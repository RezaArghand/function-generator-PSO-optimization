import math
import random
import numpy as np
import parameters as par
import sympy as sp
import functions as func
from scipy.stats import logistic

mainList = par.finalLib
x0 = sp.symbols("x0")


def mainCost(position):
    theString = []

    for i in position:
        theString.append(mainList[i])
    finalString = "".join(func.makeBalanced(theString))

    if ('x0' in theString):
        try:
            # if 'x0' in theString:
            #     theString += ''
            # else:
            #     theString += '-x0*5000'

            mainFunc = eval(finalString)
            # print(mainFunc)
            firstCost = abs(func.evalFunction(1, finalString) - 1) + abs(
                func.evalFunction(4, finalString) - 2) + abs(
                func.evalFunction(16, finalString) - 4)
            # print(firstCost)
            steps = 100
            maxY = 5
            dx = maxY / steps
            secondCost = 0

            # for i in range(0, steps):
            #     xx = dx * i
            #     f1 = (func.evalFunction(xx + dx, finalString) - func.evalFunction(xx, finalString)) ** 2
            #     f2 = dx ** 2
            #     f3 = np.sqrt(f1 + f2)
            #     secondCost = secondCost + f3
            #
            # result = (100 * firstCost + abs(secondCost)) / 1000
            result = firstCost * 100
        except:
            result = 10000
            mainFunc = func.makeBalanced(theString)
    else:

        result = 15000
        mainFunc = "there is no valid function"

    return result, mainFunc


def costNumber(positon):
    final, funn = mainCost(positon)
    return final


def bestFunc(position):
    final, funn = mainCost(position)
    result = "y = " + str(funn)
    return result

# pp = [1, 19, 11, 9, 24]
#
# print(str(bestFunc(pp)))

# x = sp.symbols("x")
#
# x = 2
# h = eval('4*x')
# print(h)
# print(func.sigmoid(5.6))
# print(sp.N(sp.tan(7 - sp.cos(8))))
