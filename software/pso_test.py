import random

def pso(n_particles, dimensions, search_space, max_iter):
    # Initialize the particles
    particles = []
    for i in range(n_particles):
        particle = {
            'position': [random.uniform(search_space[d][0], search_space[d][1]) for d in range(dimensions)],
            'velocity': [0 for _ in range(dimensions)],
            'pbest': [0 for _ in range(dimensions)],
            'pbest_value': float('inf')
        }
        particles.append(particle)
    gbest = particles[0]

    # PSO loop
    for _ in range(max_iter):
        for particle in particles:
            # Update personal best
            particle['pbest_value'] = evaluate(particle['pbest'])
            if evaluate(particle['position']) < particle['pbest_value']:
                particle['pbest'] = particle['position'][:]
            
            # Update global best
            if particle['pbest_value'] < evaluate(gbest['position']):
                gbest = particle

            # Update velocity and position
            w = 0.5
            c1 = 2
            c2 = 2
            for i in range(dimensions):
                r1 = random.random()
                r2 = random.random()
                particle['velocity'][i] = w * particle['velocity'][i] + c1 * r1 * (particle['pbest'][i] - particle['position'][i]) + c2 * r2 * (gbest['position'][i] - particle['position'][i])
                particle['position'][i] += particle['velocity'][i]
    
    return gbest

def evaluate(position):
    # Calculate the value of the Beale function at the given position
    x = position[0]
    y = position[1]
    return (1.5 - x + x*y)**2 + (2.25 - x + x*y**2)**2 + (2.625 - x + x*y**3)**2

# Test the PSO algorithm
result = pso(100, 2, [[-4.5, 4.5] for _ in range(2)], 1000)
print(result)