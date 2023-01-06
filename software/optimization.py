from pso.optimize_helpers import Particle, accuracy, consist
import numpy as np
from load_cell.mass import measure_mass
from cv.dimensions import image_process, edges, analyze_edge, find_dim

# Settings
numParticles = 10 # not sure

# Array of particle objects
particles = []

# Inertia weights?


# Execute iteration
def optimize(func, xmax, xmin, xguess, numDimensions, iter): #inputs should be the fitness of last iteration
    
    # global optimum
    x_best_g = []

    for i in range(numParticles):
        # Add new particle to particle array
        particles.append(Particle(xmax[i], xmin[i], xguess[i], numDimensions))

    # For each iteration, iterate through all particles and collect data
    for j in range(numParticles):
            
        # Generate new values for the next iteration based on previous iteration
        particles[j].updateVelocity(x_best_g)
        particles[j].updatePosition()

        # compare global op to local op
    
    
    # Once print finishes, check weight, 
    mass = measure_mass()

    # check dimensions
    blurred = image_process()
    edge = edges(blurred)
    find_dim(analyze_edge(edge), edge)
    widths = find_dim(iter)[0]
    lengths = find_dim(iter)[1]

    fitness = func(mass, widths, lengths, 0.33, 0.5, 200)

    return 


# Fitness Functions
def fitness(mass, widths, lengths, mass_desired, width_desired, length_desired): # width is a list of measurements for the plane or cube

    return 0.2*consist(widths, lengths) + 0.2*accuracy(average(widths), width_desired)+ 0.1*accuracy(average(lengths), length_desired) + 0.5*accuracy(mass, mass_desired)

def average(list): 
    for i in list: 
        sum =+ i
    return sum/list.len()