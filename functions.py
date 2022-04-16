# Function to check parentheses
import math
import random
import numpy as np
import sympy as sp
from matplotlib import pyplot as plt
import itertools


def isBalanced(myStr):
    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return True
    else:
        return False


def makeBalanced(str):
    while isBalanced(str) == False:
        str += ')'
    return str


def variableMaker(variableNum):
    result = []
    for i in range(variableNum):
        s = str(i)
        ss = 'x' + s
        result.append(ss)
    return result


def realNumberGenerator(minn, maxx):
    return random.randint(minn, maxx) * random.random()


def sigmoid(input):
    result = 1 / (1 + np.exp(-input))
    return result


def evalFunction(a, function):
    x0 = a
    # result = sp.N(eval(function))
    result = eval(function)
    return result


def normalizeLength(f1, f2):
    length1 = len(f1)
    length2 = len(f2)
    nothing = ['']
    finalLib = []
    maxLen = max(length1, length2) * 3 + 1
    newF1 = (maxLen // length1) * f1 + (maxLen % length1) * nothing
    newF2 = (maxLen // length2) * f2 + (maxLen % length2) * nothing
    # newF3 = (maxLen // length3) * f3 + (maxLen % length3) * nothing
    # for i in range(maxLen):
    #     finalLib.append(newF1[i])
    #     finalLib.append('')
    #     finalLib.append(newF2[i])
    #     finalLib.append('')
    #     finalLib.append(newF3[i])
    #     finalLib.append('')
    #     finalLib.append("1")
    finalLib = newF1 + newF2
    return maxLen, finalLib


def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


def combinationGenerator(rangeNumber, lengthNumber):
    print("generating combinations of answers___replacement is allowed")
    mainList = [i for i in range(rangeNumber)]
    result = list(itertools.combinations_with_replacement(mainList, lengthNumber))
    # for c in itertools.combinations_with_replacement(mainList, n):
    #     f = open("combination.txt", "a")
    #
    #     f.write(str(c))
    #     f.write(',')
    #     f.close()
    sizeOfResult = np.size(result)
    # random.shuffle(result)
    # print(result)
    print("combination list size = " + str(sizeOfResult))
    print(result[10])
    return result


def map_value(in_v, in_min, in_max, out_min, out_max):  # (3)
    """Helper method to map an input value (v_in)
       between alternative max/min ranges."""

    v = out_min + ((out_max - out_min) / (in_max - in_min)) * (in_v - in_min)
    if v < out_min or v > out_max:
        v = out_max - out_min / in_max
        print('maping error ocuured! #######################################')

    # result = int(np.floor(v))
    return v


def mamalSorting(position):
    sortedArray = sorted(range(len(position)), key=lambda k: position[k])
    omitableMembers = []
    for i in range(len(position)):
        if position[i] < 0 or position[i] == 0:
            omitableMembers.append(int(i))
    for i in omitableMembers:
        sortedArray.remove(i)
    result = sortedArray
    return result


def simplifyFunction(functionString):
    x0 = sp.symbols("x0")
    np.tanh = sp.symbols("np.tanh")
    result = sp.simplify(eval(functionString))
    return result

# print('((+-np.tanh( + 589.01 +  + -64.09 + +np.tanh( + -277.75 +  + -184.49 + np.tanh( + 259.69 + (np.tanh(-x0 + -289.99 +  + -254.33 +  + -294.25 +  + -56.78 +  + 23.12 +  + -176.02 + np.tanh(x0))))))))')
# print(simplifyFunction('((+-np.tanh( + 589.01 +  + -64.09 + +np.tanh( + -277.75 +  + -184.49 + np.tanh( + 259.69 + (np.tanh(-x0 + -289.99 +  + -254.33 +  + -294.25 +  + -56.78 +  + 23.12 +  + -176.02 + np.tanh(x0))))))))'))
# print(simplifyFunction('sp.tanh(x0)-12*x0+23*x0'))
# print((map_value(35.6, -150, 150, 0, 1356)))
# print(evalFunction(25, 'np.sin(x0)'))
# print(math.sin(25))
# pos = [5, -4, -3, 2, 1]
# print(mamalSorting(pos))
# x0 = sp.symbols("x0")
# combinationGenerator(14, 5)
# print(eval('np.sin(10)*x0'))
