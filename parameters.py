import random

import functions as func

number_of_function_variables = 1  # result function's variable count
# function library
funcLib = ['', 'np.sin(x0)', 'np.cos(x0)',
           'np.exp(x0)', 'np.exp(x0', 'np.sqrt(x0)', 'np.sqrt(x0', 'x0', 'np.sin(x0', 'np.cos(x0',
           'np.exp(x0', 'np.sin(', 'np.cos(', 'np.tan(', 'np.sqrt(x0', '1.0', '']
operators = ['*', '*', '/', '+', '-', ')', '', '1']
realNum = ['', '']
maxVariable, finalLib = func.normalizeLength(funcLib, operators, realNum)
# random.shuffle(finalLib)
print(finalLib)
# end function library
# print(finalLib.index(')'))

# parameters of PSO optimization algorithm
number_of_particles = 200  # particle count
number_randomize_particles = 50
# firstNumCount = 5
# secondNumCount = 5
# functionNum = 1
# firstOperationNum = 1
# secondOperationNum = 1
# thirdOperation = 1
funcNum = 5
varNum = funcNum * 2  # number of parameters in each particle
damping_rate_W = 0.9  # inertia damper
max_of_variable = len(finalLib) - 1  # max domain
min_of_variable = -len(finalLib) + 1  # min domain
bound_of_realNumber = 5
satisfaction_cost_number = 1.0e-2  # satisfaction point
W = 0.9  # inertia
C1 = 1.1  # cognitive (particle)
C2 = 1.6  # social (swarm)
max_iteration_number = 80000  # max iteration
# end parameters of PSO optimization

# ll = [1, 1, 1, 1, 1, 1]
# print(len(ll))
