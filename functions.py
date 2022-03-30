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


def combinationGenerator(n):
    print("generating combinations of answers___replacement is allowed")
    mainList = [i for i in range(n)]
    result = list(itertools.combinations_with_replacement(mainList, n))
    sizeOfResult = np.size(result)
    random.shuffle(result)
    print("combination list size = " + str(sizeOfResult))
    print(result[0])
    return result


def map_value(in_v, in_min, in_max, out_min, out_max):  # (3)
    """Helper method to map an input value (v_in)
       between alternative max/min ranges."""

    v = (in_v - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    if v < out_min:
        v = out_min
    elif v > out_max:
        v = out_max

    # result = int(np.floor(v))
    return v

# print((map_value(35.6, -150, 150, 0, 1356)))
# print(evalFunction(25, 'np.sin(x0)'))
# print(math.sin(25))
