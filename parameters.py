import functions as func

number_of_function_variables = 1  # result function's variable count
# function library
funcLib = ['sp.sin(', 'sp.cos(', 'sp.tan(', 'sp.cot(', 'sp.exp(', 'sp.sqrt(', 'x0']
operators = ['*', '/', '+', '-', '**', ')']
realNum = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
nothing = ['']
maxVariable, newFuncLib, newOperators, newRealNum = func.normalizeLength(funcLib, operators, realNum)
maxVariable += 1
finalLib = newFuncLib + newOperators + newRealNum
print(finalLib)
# end function library
# print(finalLib.index(')'))

# parameters of PSO optimization algorithm
number_of_particles = 50  # particle count
# firstNumCount = 5
# secondNumCount = 5
# functionNum = 1
# firstOperationNum = 1
# secondOperationNum = 1
# thirdOperation = 1
varNum = 8  # number of parameters in each particle
damping_rate_W = 0.9  # inertia damper
max_of_variable = len(finalLib) - 1  # max domain
min_of_variable = 0  # min domain
satisfaction_cost_number = 1.0e-200  # satisfaction point
W = 0.99  # inertia
C1 = 0.8  # cognitive (particle)
C2 = 1.1  # social (swarm)
max_iteration_number = 150000  # max iteration
# end parameters of PSO optimization

# ll = [1, 1, 1, 1, 1, 1]
# print(len(ll))
