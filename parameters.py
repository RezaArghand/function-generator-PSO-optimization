import random

import functions as func

# parameters of PSO optimization algorithm
number_of_particles = 1500  # particle count
number_randomize_particles_fullArea = 500
number_randomize_particles_firstBitOfBest = 500

funcNum = 5
varNum = funcNum * 2 + 1  # number of parameters in each particle
damping_rate_W = 0.9  # inertia damper
w_reset_iteration = 1500  # the iteration that w is reset
bound_of_realNumber = 50
satisfaction_cost_number = 0.5  # satisfaction point
W = 0.9  # inertia
C1 = 1.1  # cognitive (particle)
C2 = 1.6  # social (swarm)
max_iteration_number = 80000  # max iteration
# end parameters of PSO optimization

# function library
funcLib = ['(', 'np.sin(', 'np.exp(', 'np.sqrt(', 'np.floor(', 'np.floor(x0', 'np.sqrt(x0', 'x0', 'np.cos(x0',
           'np.tan(', 'np.sqrt(x0', '(x**2)', 'np.exp(', 'np.exp(x0',
           '1/x0', 'np.sign(', 'np.sign(x0',
           '(x0 ** 3)', '']
operators = ['*', '/', '+', '-', '**', ')', '(']
# maxVariable, finalLib = func.normalizeLength(funcLib, operators)
finalLib = funcLib + operators
max_of_variable = len(finalLib) - 1  # max domain
min_of_variable = -len(finalLib) + 1  # min domain

print(finalLib)

# defining combination tuples:

combinationList = func.combinationGenerator(varNum + 1)
combinationListLength = len(combinationList)
