import random

import numpy as np

import functions as func

# parameters of PSO optimization algorithm
number_of_particles = 200  # particle count
number_randomize_particles_fullArea = int(np.floor(0.25 * number_of_particles))
number_randomize_particles_firstBitOfBest = int(np.floor(0.25 * number_of_particles))

funcNum = 5
varNum = funcNum * 2 + 1  # number of parameters in each particle
damping_rate_W = 0.9  # inertia damper
w_reset_iteration = 1500  # the iteration that w is reset
bound_of_realNumber = 1000
satisfaction_cost_number = 0.005  # satisfaction point
W = 0.9  # inertia
C1 = 1.6  # cognitive (particle)
C2 = 2.4  # social (swarm)
max_iteration_number = 80000  # max iteration
# end parameters of PSO optimization

# function library
# funcLib = ['(', 'np.sin(', 'np.exp(', 'np.sqrt(', 'np.floor(', 'np.floor(x0', 'np.sqrt(x0', 'x0', 'np.cos(x0',
#            'np.tan(', 'np.sqrt(x0', '(x**2)', 'np.exp(', 'np.exp(x0', 'np.tanh(x0)', 'np.tan(x0)',
#            'np.sign(', 'np.sign(x0', 'np.tanh(', 'np.tanh(x0', 'np.sinh(x0',
#            '(x0 ** 3)', '', 'np.log(', 'np.log(x0)', 'np.log(x0', 'abs(', 'np.pi']
# operators = ['*', '/', '+', '-', '**', ')', '(']
# 'np.log(x0', 'np.tanh(x0', 'np.sqrt(x0', 'abs(x0','np.log(', 'np.tanh(', 'np.sqrt(', 'abs(', 'np.pi'

funcLib = ['np.tanh(', 'x0', 'np.tanh(x0']
operators = ['*', '+', '-', ')', '(', '']
# maxVariable, finalLib = func.normalizeLength(funcLib, operators)
finalLib = funcLib + operators
max_of_variable = len(finalLib) - 1  # max domain
min_of_variable = -len(finalLib) + 1  # min domain

print(finalLib)

# defining combination tuples:

combinationList = func.combinationGenerator(varNum + 1)
combinationListLength = len(combinationList)
