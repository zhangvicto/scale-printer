import numpy as np

# Particle object
class Particle: 
    def __init__(self, pos, vel, index): 
        x = pos # position
        # y = 0 
        v = vel # velocity
        index = index
    pbest = 0 # personal best 
    positions = []


# Function for creating new particle
def newParticle(xguess, xmax, xmin, rp, particles): 
    # Generate initial values for position and velocity
    pos = np.random.uniform(max(xguess-rp/2, xmin), min(xguess-rp/2, xmax))
    vel = np.random.uniform(-abs(xmax-xmin), abs(xmax-xmin))

    # Create new particle based on the initial parameters
    p = Particle(pos, vel)

    # Add initial position to new particle's positions array
    p.positions.append(pos)

    # Add particle to particle array
    particles.append(p)

    # Return index of the object
    return particles.index(p)
