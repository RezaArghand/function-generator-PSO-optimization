import math
import random
import numpy as np
import parameters as par
import sympy as sp
import functions as func
from scipy.stats import logistic

x0 = sp.symbols("x0")
x1 = sp.symbols("x1")


def mainCost(position):
    # combinations = par.combinationList
    # combinationsLength = len(combinations)
    # mainLib = par.finalLib
    # inputt = []
    # theString = []
    # inputt.append('')
    # l_num_func = int(len(position) - 1)
    # l_func = int(l_num_func / 2)
    # combinationNumber = int(
    #     np.floor(func.map_value(position[-1], par.min_of_variable, par.max_of_variable, 0, combinationsLength - 1)))
    # combinationList = combinations[combinationNumber]
    # for i in range(l_func):
    #     j = int(np.floor(position[i]))
    #     inputt.append(mainLib[j])
    # for i in range(l_func, l_num_func):
    #     value = func.map_value(position[i], par.min_of_variable, par.max_of_variable, -par.bound_of_realNumber,
    #                            par.bound_of_realNumber)
    #     stringValue = '+ ' + str(round(value, 2))
    #     inputt.append(stringValue)
    # inputt.append('')
    # for i in combinationList:
    #     theString.append(inputt[i])
    # # print(position)
    # # print(inputt)
    # # print(combinationList)
    # # print(theString)
    # # a = input("go?")
    # # finalString = "".join(func.makeBalanced(theString))
    # primaryString = "".join(theString)
    # finalString = func.makeBalanced(primaryString)
    finalString = func.functionStringGenerator(position)
    if 'x0' in finalString and 'x1' in finalString:
        try:
            # if 'x0' in theString:
            #     theString += ''
            # else:
            #     theString += '-x0*5000'

            steps = 200
            maxY = 20
            dx = maxY / steps
            mainX = np.linspace(-20, 20, 30)
            mainY = np.linspace(-20, 20, 30)
            secondCost = 0
            for i in range(len(mainX)):
                xx = mainX[i]
                for j in range(len(mainY)):
                    yy = mainY[i]
                    primaryVal = np.sin(xx) * np.cos(yy) + 1.35
                    secondCost += abs(func.evalFunctionDualFunc(xx, yy, finalString) - primaryVal)
            # for j in range(len(mainY)):
            #     yy = mainY[j]
            #     for i in range(len(mainX)):
            #         xx = mainX[i]
            #         primaryVal = np.sin(xx) * np.cos(yy) + 1.35
            #         secondCost += abs(func.evalFunctionDualFunc(xx, yy, finalString) - primaryVal)
            # secondCost = secondCost / steps
            result = secondCost
            # print(position)
            # result = firstCost
            # mainFunc = str(sp.simplify(eval(finalString)))  # eval(finalString)
            mainFunc = finalString
        except:
            result = 10000
            mainFunc = "error(1) : " + finalString
    else:
        result = 15000
        mainFunc = "error(2) : " + finalString

    return result, mainFunc


def costNumber(positon):
    final, funn = mainCost(positon)
    return final


def bestFunc(position):
    x0 = sp.symbols('x0')
    x1 = sp.symbols('x1')
    funn = func.functionStringGenerator(position)
    try:
        result1 = str(eval(funn))
    except:
        result1 = str(funn)
    result = "Y = " + str(result1)
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
