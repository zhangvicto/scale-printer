from pso.optimize_helpers import Particle, accuracy, consist
import numpy as np
from load_cell.mass import measure_mass, tare
from gcode_gen.generate import gcode_gen, genStart, genEnd, settings, square_size
from gcode_sender.printcore_gcode_sender import send_gcode
from cv.dimensions import image_process, edges, analyze_edge, find_dim
from time import perf_counter

# Settings
numParticles = 10

# Execute iteration
def optimize(mode, xmax, xmin, xguess, mass_desired, numDimensions, iteration): #inputs should be the fitness of last iteration
    
    # global optimum
    particles = []
    mass_data = []
    dimension_data = []
    x_best_g = []

    # Create Particle Array
    for i in range(0, numParticles):
        # Add new particle to particle array
        particle = Particle(xmax, xmin, xguess, numDimensions)
        particles.append(particle)

    # STARTING THE ITERATION
    
    # For each particle, print and collect data
    particle_i = 0 # particle index

    last_mass = 0 

    for particle in particles:

        iter = particle_i + 1
        time_start = perf_counter()


        # MEASUREMENT STUFF

        # creep = 0.0005*5000/(3*60)*4 # grams/sec * 4 load cells

        # Generate Gcode
        with open("./gcode_gen/test.gcode", "w") as f:
            
            gcode = genStart(iter=iter, nozzleD=0.4, Te=xguess[0], Tb=0) # bed is disabled
            gcode += gcode_gen(mode, iter, {'moveSpeed': xguess[1], 'extMult': xguess[2]}) # generate gcode with custom parameters
            gcode += genEnd()

            f.write(gcode)
        
        print("Gcode Generated. \n")

        # Tare Weight before Starting Print
        # time_zero = perf_counter() - time_start
        # print("Initial weight offset: {}".format(time_zero))
        
        zero_weight = 0 

        # Taring
        if iter == 1: 
            zero_weight = tare()
        print("Initial weight offset: {}".format(zero_weight))

        # Account for Creep - ignoring creep for now
        initial_zero = zero_weight #- time_zero*creep

        # Pass in Printing Parameters
        print("Sending Gcode to Printer. \n")
        send_gcode(iter, './gcode_gen/test.gcode')

        # measure_time = perf_counter() - time_zero

        # Once print finishes, check weight
        print("Measuring Mass. \n")
        mass = measure_mass()
        mass_real = mass - last_mass - initial_zero # find weight of print
        mass_data.append(mass_real)


        last_mass = mass


        # CV STUFF

        # Find Dimension of the Print
        print("Starting CV Process. \n")
        img = image_process() # Process Image
        edge = edges(img) # Canny Edge Detection

        distX = analyze_edge(edge) # Get the bed x-axis length in terms of pixels

        x=[]
        y=[]

        # Calculate Print Location
        if distX is not None:
            ratio = distX/255 # Pixels per mm
            print('Ratio: {}'.format(ratio))
            # Pixel = mm * ratio

            if mode == 'L': 
                if distX > 0: 
                    xOffset = 20
                    x1 = xOffset + round((iter-1)*15*ratio)
                    x2 = round(x1 + 10*ratio)
                    x = [x1, x2]
                    # print(x)
                    # print(x)
                    y1 = round(180*ratio) - 20
                    y2 = round(180*ratio)
                    y = [y1, y2]
                else: 
                    x = [None, None]
                    y = [None, None]

            if mode == 'P': 
                if distX: 
                    initial_gap = 10
                    gap = 10
                    x1 = round((initial_gap + gap/2 + (iter-1)*square_size)*ratio)
                    x2 = round(x1 + (square_size + gap)*ratio)
                    x = [x1, x2]
                    # print(x)
                    yOffset = -5
                    y1 = round((200 - (square_size + gap + yOffset))*ratio)
                    y2 = round((200- yOffset)*ratio)
                    y = [y1, y2]
                    # print(y)
                else: 
                    x = [None, None]
                    y = [None, None]
            
            if mode == 'C': 
                x = [None, None]
                y = [None, None]

        dimensions = find_dim(x, y, distX, edge, iter) # Find dim

        if dimensions is not None: 
            widths = dimensions[0]
            lengths = dimensions[1]
            dimension_data.append(dimensions)
        else: 
            dimension_data.append(None)
        
        # Print all data
        print("Mass: {}. Dimensions: {}. Time Elasped: {}.".format(mass_data, dimension_data, perf_counter() - time_start))


        # PSO STUFF

        # Evaluate and compare particle global optimum to local optimum
        # Calculate Current Fitness
        particle.f_best_p = fitness(mode, dimensions[0], dimensions[1], mass, mass_desired, square_size, square_size)
        print("Fitness: {}".format(particle.fitness))

        if iter == 1:
            x_best_g = particle.x_best_p[:] # Set global optimum to first particle
            f_best_g = particle.f_best_p # set global optimum to first particle
        else: 
            if particle.f_best_p < f_best_g: # Compare particle fitness to group fitness
                x_best_g = particle.x_best_p[:] # Splice array and set global op to current particle

        # Generate new values for the next iteration based on previous iteration
        particle.updateVelocity(x_best_g)
        particle.updatePosition()

        print("Particle Position: {}".format(particle.x_best_p))
        
        # NEXT PARTICLE
        particle_i += 1

    
    print('Iteration {} complete.'.format(iteration))

    return particle.x_best_p


# Fitness Functions
def fitness(mode, widths, lengths, mass, mass_desired, width_desired, length_desired): # width is a list of measurements for the plane or cube
    if mode == "L": 
        return 0.2*consist([widths, lengths]) + 0.2*accuracy(average(widths), width_desired)+ 0.1*accuracy(average(lengths), length_desired) + 0.5*accuracy(mass, mass_desired)

    elif mode == "P": 
        return 0.1*accuracy(widths, width_desired)+ 0.1*accuracy(lengths, length_desired) + 0.7*accuracy(mass, mass_desired)
    
    elif mode == "C":
        return 0
    
def average(list): 
    for i in list: 
        sum =+ i
    
    return sum/list.len()
