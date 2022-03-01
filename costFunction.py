import math
import random
import numpy as np
import parameters as par
import sympy as sp
import functions as func
from scipy.stats import logistic

x0 = sp.symbols("x0")


def mainCost(input):
    position = []
    newPosition = []
    for i in range(0, par.funcNum):
        position.append(abs(math.floor(input[i])))
        newPosition.append(input[i + par.funcNum] * par.bound_of_realNumber / par.max_of_variable)
    theString = []
    mainList = par.finalLib
    for i in range(len(position)):
        realN = str(newPosition[i])
        theString.append("+")
        theString.append(realN)
        theString.append("*")
        theString.append(mainList[position[i]])
    # finalString = "".join(func.makeBalanced(theString))
    sstring = "".join(theString)
    finalString = func.makeBalanced(sstring)

    if ("x0" in finalString):
        try:
            # if 'x0' in theString:
            #     theString += ''
            # else:
            #     theString += '-x0*5000'

            # eval(finalString)
            steps = 1000
            maxY = 100
            dx = maxY / steps
            secondCost = 0

            for i in range(0, steps):
                xx = dx * i
                secondCost += abs(func.evalFunction(xx, finalString) - (5.7 * np.sin(xx ** 2) - 11 * xx + 5))
            # secondCost = secondCost / steps
            result = secondCost
            # print(position)
            # result = firstCost
            mainFunc = sp.simplify(eval(finalString))
        except:
            result = 1000000
            mainFunc = "error calculating the function generated..."
    else:
        result = 1500000
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
