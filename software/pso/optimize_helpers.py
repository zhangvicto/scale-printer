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
def newParticle(xguess, xmax, xmin, rp): 
    # Generate initial values for position and velocity
    pos = np.random.uniform(max(xguess-rp/2, xmin), min(xguess-rp/2, xmax))
    vel = np.random.uniform(-abs(xmax-xmin), abs(xmax-xmin))

    # Create new particle based on the initial parameters
    p = Particle(pos, vel)

    # Add initial position to new particle's positions array
    p.positions.append(pos)

    # Return index of the object
    return p

# Deviation of measurement from desired value
def diff(xm, xd): 
    return abs(xm-xd)/xd

# Consistency (average deviation)
def consist(array): 
    return np.std(array)