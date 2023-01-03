from pso.optimize_helpers import Particle, accuracy, consist
import numpy as np
from load_cell.mass import load_cell_setup, measure_mass
from cv.camera import measure_dim

# Settings
numParticles = 10 # not sure

# Array of particle objects
particles = []

# Variables MIN MAX
TeMax = 260
TeMin = 200

TbMax = 80
TbMin = 40

VpMax = 80
VpMin = 10

EfMax = 0.8
EfMin = 1.2

xmax = [TeMax, TbMax, VpMax, EfMax]
xmin = [TeMin, TbMin, VpMin, EfMin]
xguess = []

numDimensions = len(xmax)

# Inertia weights?

# Optimization functions


# Execute iteration
def optimize(func, xmax, xmin, xguess, numDimensions): #inputs should be the fitness of last iteration
    
    # global optimum
    x_best_g = []

    for i in range(numParticles):
        # Add new particle to particle array
        particles.append(Particle(xmax[i], xmin[i], xguess[i], numDimensions))

        # Once print finishes, check weight, 
        load_cell_setup()
        mass = measure_mass()

        # check dimensions
        measure_dim()


    # For each iteration, iterate through all particles and collect data
    for j in range(numParticles):
            
        # Generate new values for the next iteration based on previous iteration
        particles[j].updateVelocity(x_best_g)
        particles[j].updatePosition()

        # of iteration 
        # compare global op to local+


# Fitness Functions
def fitness(mass, widths, lengths, mass_desired, width_desired, length_desired): # width is a list of measurements for the plane or cube

    return 0.2*consist(widths, lengths) + 0.2*accuracy(average(widths), width_desired)+ 0.1*accuracy(average(lengths), length_desired) + 0.5*accuracy(mass, mass_desired)

def average(list): 
    for i in list: 
        sum =+ i
    return sum/list.len()