import random

import numpy as np
import combinations_15
import functions as func

# parameters of PSO optimization algorithm
number_of_particles = 200  # particle count
number_randomize_particles_fullArea = int(np.floor(0.25 * number_of_particles))
number_randomize_particles_firstBitOfBest = int(np.floor(0.25 * number_of_particles))

damping_rate_W = 0.9  # inertia damper
w_reset_iteration = 30000  # the iteration that w is reset
bound_of_realNumber = 1000
satisfaction_cost_number = 0.5  # satisfaction point
W = 0.9  # inertia
C1 = 1.6  # cognitive (particle)
C2 = 2.4  # social (swarm)
max_iteration_number = 80000  # max iteration
# end parameters of PSO optimization

# function library
# funcLib = ['', 'np.sin(', 'np.exp(', 'np.sqrt(', 'np.floor(', 'x0', 'np.tan(', 'np.sign(']
# operators = ['*', '/', '+', '-', '**', ')', '(']

funcLib = ['', '', 'np.tanh(', 'tanh(x0']
operators = ['*', '+', '-', ')', '(', '', '']
# maxVariable, finalLib = func.normalizeLength(funcLib, operators)
finalLib = 3 * (10 * funcLib + 5 * operators)
numberCounts = 5
lengthOfFunctionResult = 10

# defining combination tuples:

dimention = 20
max_of_variable = len(finalLib) - 1  # max domain
min_of_variable = -len(finalLib) + 1  # min domain
