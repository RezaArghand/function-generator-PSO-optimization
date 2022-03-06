import math
import random
import numpy as np
import parameters as par
import sympy as sp
import functions as func
from scipy.stats import logistic

x0 = sp.symbols("x0")


def mainCost(position):
    combinations = par.combinationList
    combinationsLength = len(combinations)
    mainLib = par.finalLib
    inputt = []
    theString = []
    inputt.append('')
    l_num_func = int(len(position) - 1)
    l_func = int(l_num_func / 2)
    combinationNumber = int(
        np.floor(func.map_value(position[-1], par.min_of_variable, par.max_of_variable, 0, combinationsLength - 1)))
    combinationList = combinations[combinationNumber]
    for i in range(l_func):
        j = int(np.floor(position[i]))
        inputt.append(mainLib[j])
    for i in range(l_func, l_num_func):
        value = func.map_value(position[i], par.min_of_variable, par.max_of_variable, -par.bound_of_realNumber,
                               par.bound_of_realNumber)
        inputt.append(str(round(value, 2)))
    inputt.append('')
    for i in combinationList:
        theString.append(inputt[i])
    # print(position)
    # print(inputt)
    # print(combinationList)
    # print(theString)
    # a = input("go?")
    # finalString = "".join(func.makeBalanced(theString))
    primaryString = "".join(theString)
    finalString = func.makeBalanced(primaryString)

    if ("x0" in finalString):
        try:
            # if 'x0' in theString:
            #     theString += ''
            # else:
            #     theString += '-x0*5000'

            mainFunc = finalString  # eval(finalString)
            steps = 1000
            maxY = 100
            dx = maxY / steps
            secondCost = 0

            for i in range(0, steps):
                xx = dx * i
                secondCost += abs(func.evalFunction(xx, finalString) - (2.35 * np.sqrt(xx)))
            # secondCost = secondCost / steps
            result = secondCost
            # print(position)
            # result = firstCost
        except:
            result = 10000
            mainFunc = finalString
    else:
        result = 15000
        mainFunc = finalString

    return result, mainFunc


def costNumber(positon):
    final, funn = mainCost(positon)
    return final


def bestFunc(position):
    final, funn = mainCost(position)
    try:
        result1 = sp.simplify(eval(funn))
    except:
        result1 = str(funn)
    result = "y = " + str(result1)
    return result

# pp = [1, 5, 11, 9, 12, 10, 1]
# #
# print(str(costNumber(pp)))

# x = sp.symbols("x")
#
# x = 2
# h = eval('4*x')
# print(h)
# print(func.sigmoid(5.6))
# print(sp.N(sp.tan(7 - sp.cos(8))))
