import random

import numpy as np
import functions as func

# parameters of PSO optimization algorithm
number_of_particles = 200  # particle count
number_randomize_particles_fullArea = int(np.floor(0.2 * number_of_particles))

damping_rate_W = 0.9  # inertia damper
w_reset_iteration = 1500  # the iteration that w is reset
bound_of_realNumber = 10000
satisfaction_cost_number = 0.005  # satisfaction point
W = 0.9  # inertia
C1 = 1.6  # cognitive (particle)
C2 = 2.4  # social (swarm)
max_iteration_number = 80000  # max iteration
# end parameters of PSO optimization

# function library
# funcLib = ['', 'np.sin(', 'np.exp(', 'np.sqrt(', 'np.floor(', 'x_0 ', 'x_1 ', 'np.tan(', 'np.sign(', 'np.sin(x_0 ',
#            'np.exp(x_0 ', 'np.sqrt(x_0 ', 'np.floor(x_0 ', 'x_0 ', 'np.tan(x_0', 'np.sign(x_0', 'np.tanh(',
#            'np.tanh(x_ 0)',
#            'np.sin(x_1 ', 'np.exp(x_1 ', 'np.sqrt(x_1 ', 'np.floor(x_1 ', 'np.tan(x_1 ', 'np.sign(x_1 ', 'np.tanh(',
#            'np.tanh(x_1) ']
funcLib = ['', 'np.sin(', 'np.exp(', 'np.sqrt(', 'np.floor(', 'x_0 ', 'x_1 ','x_2', 'np.tan(', 'np.sign(','np.tanh(']

operators = ['*', '/', '+', '-', '**', ')', '(']

# maxVariable, finalLib = func.normalizeLength(funcLib, operators)
finalLib = (funcLib + operators)
numberCounts = 5
lengthOfFunctionResult = 10

# defining combination tuples:

dimention = 60
max_of_variable = len(finalLib) - 1  # max domain
min_of_variable = -len(finalLib) + 1  # min domain
