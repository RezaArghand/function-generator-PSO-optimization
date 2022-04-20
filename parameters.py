import random

import numpy as np
import functions as func

# parameters of PSO optimization algorithm
number_of_particles = 200  # particle count
number_randomize_particles_fullArea = int(np.floor(0.5 * number_of_particles))

damping_rate_W = 0.9  # inertia damper
w_reset_iteration = 1500  # the iteration that w is reset
bound_of_realNumber = 10000
satisfaction_cost_number = 0.01  # satisfaction point
W = 0.9  # inertia
C1 = 1.6  # cognitive (particle)
C2 = 2.4  # social (swarm)
max_iteration_number = 80000  # max iteration
# end parameters of PSO optimization

# function library
funcLib = ['', 'np.sin(', 'np.exp(', 'np.sqrt(', 'np.floor(', 'x0', 'np.tan(', 'np.sign(', 'np.sin(x0', 'np.exp(x0',
           'np.sqrt(x0', 'np.floor(x0', 'x0', 'np.tan(x0', 'np.sign(x0', 'np.tanh(', 'np.tanh(x0)']
operators = ['*', '/', '+', '-', '**', ')', '(']

# funcLib = ['', 'np.tanh(', 'tanh(x0', 'x0']
# operators = ['*', '+', '-', ')', '(', '']
# maxVariable, finalLib = func.normalizeLength(funcLib, operators)
finalLib = (funcLib + operators)
numberCounts = 5
lengthOfFunctionResult = 10

# defining combination tuples:

dimention = 20
max_of_variable = len(finalLib) - 1  # max domain
min_of_variable = -len(finalLib) + 1  # min domain
