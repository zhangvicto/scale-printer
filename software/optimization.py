from pso.optimize_helpers import Particle, accuracy, consist
import numpy as np
from load_cell.mass import measure_mass
from cv.dimensions import image_process, edges, analyze_edge, find_dim

# Settings
numParticles = 10 # not sure

# Array of particle objects
particles = []

x_best_g = []
# Inertia weights?

desired_mass = 


# Execute iteration
def optimize( func, xmax, xmin, xguess, numDimensions, iter, mode): #inputs should be the fitness of last iteration
    
    # global optimum
    global x_best_g, particles

    # Create Particle Array
    for i in range(0, numParticles):
        # Add new particle to particle array
        particles.append(Particle(xmax[i], xmin[i], xguess[i], numDimensions))

    # STARTING THE ITERATION
    # For each particle, print and collect data
    particle_i = 0 
    for particle in particles:
            
        # Once print finishes, check weight, 
        mass = measure_mass()

        # check dimensions
        blurred = image_process()
        edge = edges(blurred)

        # Print Location
        if mode == 'L': 
            x = [(iter-1)*15, iter*15]
            y = [0, 180]
        # TBD
        if mode == 'P' or mode == 'C': 
            x = [0, 0]
            y = [0, 0]


        # Get dimension
        dimensions = find_dim(x, y, analyze_edge(edge), edge)
        widths = dimensions[0]
        lengths = dimensions[1]

        # Evaluate and Compare global optimum to local optimum
        particle.evaluate(func(mass, widths, lengths, 0.33, 0.5, 200))

        if particle.f_best_p > x_best_g: # evaluate 
            x_best_g = particle.f_best_p[:]

        # Generate new values for the next iteration based on previous iteration
        particle.updateVelocity(x_best_g)
        particle.updatePosition()

        particle_i += 1

    return particles


# Fitness Functions
def fitness(mode, mass, widths, lengths, mass_desired, width_desired, length_desired): # width is a list of measurements for the plane or cube
    if mode == "L": 
        return 0.2*consist(widths, lengths) + 0.2*accuracy(average(widths), width_desired)+ 0.1*accuracy(average(lengths), length_desired) + 0.5*accuracy(mass, mass_desired)

    elif mode == "P" or mode == "C": 
        return 0
    
def average(list): 
    for i in list: 
        sum =+ i
    return sum/list.len()