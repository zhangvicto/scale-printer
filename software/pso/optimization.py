from optimize_helpers import newParticle
from optimize_helpers import 
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

# Intertia weigths?

# Optimization functions

# Generate Velocity for next iteration
def generateVelocity(index, particles): 
    return kv*particles[index].vel + kp*np.random.uniform(0, 1)*(xpbi-particles[index].x) + kg*np.random.uniform(0, 1)*(pxgi-particles[index].x)

# Execute iteration

# Create new particles
def optimize(): 
    for i in range(particles):
        newParticle()

    for i in range(numIteration): 

        # For each iteration, iterate through all particles and collect data
        for j in range(numParticles): # How many particles do we want?
            # Generate new values for the next iteration based on previous iteration
            particles[i].x =+ generateVelocity(i, particles)
