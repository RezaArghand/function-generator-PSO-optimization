import math
import random
import numpy as np
import parameters as par
import sympy as sp
import functions as func
from scipy.stats import logistic

x0 = sp.symbols("x0")


def mainCost(position):
    theString = []
    mainList = par.finalLib
    for i in position:
        theString.append(mainList[i])
    # finalString = "".join(func.makeBalanced(theString))
    sstring = "".join(theString)
    finalString = func.makeBalanced(sstring)

    if ("x0" in finalString):
        try:
            # if 'x0' in theString:
            #     theString += ''
            # else:
            #     theString += '-x0*5000'

            mainFunc = finalString  # eval(finalString)
            # print(mainFunc)
            firstCost = abs(func.evalFunction(1, finalString) - 3) + abs(
                func.evalFunction(5, finalString) - 11)
            # print(firstCost)
            steps = 1000
            maxY = 5
            dx = maxY / steps
            secondCost = 0

            for i in range(0, steps):
                xx = dx * i
                f1 = ((func.evalFunction(xx + dx, finalString)) - (func.evalFunction(xx, finalString))) ** 2
                f2 = dx ** 2
                f3 = np.sqrt(f1 + f2)
                secondCost = secondCost + f3

            result = (firstCost + abs(secondCost - 11.18) / 10)
            # result = firstCost
        except:
            result = 10000
            mainFunc = finalString
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
