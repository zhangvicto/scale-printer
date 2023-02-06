import numpy as np

# Tuning parameters
kv = 0.5
kp = 1
kg = 2

# Particle Class
class Particle: 
    def __init__(self, xmax, xmin, xguess, numDimensions): 
        self.x_i = [] # position
        self.v_i = [] # velocity
        self.x_best_p = [] # personal(local) best position
        self.f_best_p = [] # local best fitness
        self.xmax = xmax
        self.xmin = xmin
        self.numDimensions = numDimensions

        # Generate Initial Values
        for i in range(0, numDimensions): 
            pos = np.random.uniform(max(xguess[i]-r(xmax[i], xmin[i])*p(xmax[i], xmin[i], xguess[i])/2, xmin[i]), min(xguess[i]-r(xmax[i], xmin[i])*p(xmax[i], xmin[i], xguess[i])/2, xmax[i]))
            self.v_i.append(pos)
            
            vel = np.random.uniform(-abs(xmax[i]-xmin[i]), abs(xmax[i]-xmin[i]))
            self.x_i.append(vel)

    # Functions

    # Generate Velocity for next iteration
    def updateVelocity(self, x_best_g): 
        for i in range(0, self.numDimensions): 
            self.v_i[i] = kv*self.v_i[i] + kp*np.random.uniform(0, 1)*(self.x_best_p[i]-self.x_i[i]) + kg*np.random.uniform(0, 1)*(x_best_g[i]-self.x_i[i])
        
    def updatePosition(self): 
        for i in range(0, self.numDimensions): 
            self.x_i[i] =+ self.v_i[i]

            if self.x_i[i] > self.xmax[i]: 
                self.x_i[i] = self.xmax[i]
                print('Max reached')

            if self.x_i[i] < self.xmin[i]: 
                self.x_i[i] = self.xmin[i]
                print('Min reached')
                    
def r(max, min): 
    return abs(max - min)

def p(max, min, guess):
    return (max-guess)/max + (guess-min)/min

# Deviation of measurement from desired value
def accuracy(xm, xd): 
    return abs(xm-xd)/xd

# Consistency (average deviation)
def consist(array): 
    return np.std(array)
