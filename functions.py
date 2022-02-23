# Function to check parentheses
import random
import numpy as np
import sympy as sp


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


def evalFunction(x0, function):
    result = eval(function)
    return result


def normalizeLength(f1, f2, f3):
    length1 = len(f1)
    length2 = len(f2)
    length3 = len(f3)
    nothing = ['']
    maxLen = max(length1, length3, length2)
    newF1 = (maxLen // length1) * f1 + (maxLen % length1) * nothing
    newF2 = (maxLen // length2) * f2 + (maxLen % length2) * nothing
    newF3 = (maxLen // length3) * f3 + (maxLen % length3) * nothing
    return maxLen, newF1, newF2, newF3
