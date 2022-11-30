from optimize_helpers import newParticle, diff, consist
import numpy as np

# Settings
numIteration = 20 # should be determined by gcode
numParticles = 10 # not sure

# global optimum - updated every iteration
gbestX = 0

# Array of particle objects
particles = []

# Tuning parameters
kv = 0.5
kp = 1
kg = 2

# Variables MIN MAX
TeMax = 260
TeMin = 200

TbMax = 80
TeMin = 40

VpMax = 80
VpMin = 10

EfMax = 0.8
EfMin = 1.2

# Inertia weights?

# Optimization functions

# Generate Velocity for next iteration
def generateVelocity(index, particles): 
    return kv*particles[index].vel + kp*np.random.uniform(0, 1)*(xpbi-particles[index].x) + kg*np.random.uniform(0, 1)*(pxgi-particles[index].x)

# Execute iteration
def optimize(inputs): #inputs should be the fitness of last iteration
    for i in range(numParticles):
        # Add new particle to particle array

        # Extrusion Temp
        particles.append(newParticle())



    for i in range(numIteration): 

        # For each iteration, iterate through all particles and collect data
        for j in range(numParticles): # How many particles do we want?
            # Generate new values for the next iteration based on previous iteration
            particles[i].x =+ generateVelocity(i, particles)

        # of iteration 
        # compare global op to local


# Fitness Functions
def fitness(mass, widths, lengths, mass_desired, width_desired, length_desired): # width is a list of measurements for the plane or cube

    return 0.2*consist(widths, lengths) + 0.2*diff(average(widths), width_desired)+ 0.1*diff(average(lengths), length_desired) + 0.5*diff(mass, mass_desired)

def average(list): 
    for i in list: 
        sum =+ i
    return sum/list.len()