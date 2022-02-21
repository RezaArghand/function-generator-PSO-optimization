import random
import functions as func
import math

number_of_function_variables = 1  # result function's variable count
# function library
funcLib = ['sp.sin(x0)', 'sp.cos(x0)', 'sp.tan(x0)', 'sp.cot(x0)', 'sp.exp(x0)', 'sp.sqrt(x0)', 'x0']
operators = ['*', '/', '+', '-', '**']
variables = func.variableMaker(number_of_function_variables)
realNum = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
nothing = ['', '']
finalLib = funcLib + nothing
# end function library
# print(finalLib.index(')'))

# parameters of PSO optimization algorithm
number_of_particles = 120  # particle count

varNum = 10  # variable count
damping_rate_W = 0.9  # inertia damper
max_of_variable = len(finalLib) - 1  # max domain
min_of_variable = 0  # min domain
satisfaction_cost_number = 1.0e-200  # satisfaction point
W = 0.95  # inertia
C1 = 1.8  # cognitive (particle)
C2 = 2.4  # social (swarm)
max_iteration_number = 10000  # max iteration
# end parameters of PSO optimization

# ll = [1, 1, 1, 1, 1, 1]
# print(len(ll))
