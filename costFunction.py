import math
import random
import numpy as np
import parameters as par
import sympy as sp
import functions as func
from scipy.stats import logistic
import combinations_15 as mengaArray
import time
import multiprocessing
from scipy.integrate import odeint

x0 = sp.symbols("x0")


def mainCost(position):
    library = par.finalLib
    theString = []
    realNumberLib = []
    funcLib = []
    for i in range(5, 10):  # function and numbers order list
        realNum = func.map_value(position[i], par.min_of_variable, par.max_of_variable,
                                 -par.bound_of_realNumber,
                                 par.bound_of_realNumber)
        theNum = round(realNum, 4)
        mappedNumber = str(theNum)
        realNumberLib.append(mappedNumber)

    for i in range(0, 5):
        pos = int(np.floor(abs(position[i])))
        funcLib.append(library[pos])

    mainLib = funcLib + realNumberLib  # create main lib of functions and numbers
    tempOrderList = []
    for i in range(10, 20):
        tempOrderList.append(position[i])
    sortedList = func.mamalSorting(tempOrderList)
    for i in sortedList:
        theString.append(mainLib[i])

    primaryString = "".join(theString)
    finalString = func.makeBalanced(primaryString)

    if 'x0' in finalString:
        try:
            # if 'x0' in theString:
            #     theString += ''
            # else:
            #     theString += '-x0*5000'

            mainFunc = finalString  # eval(finalString)
            # ODE solution start ////////////////////////////////////////////////////////////////////////////////
            M = 1
            B = 10
            k = 20
            u = 1
            t = np.linspace(0, 5, 5000)

            y0 = [0, 0]

            def ode(y, t):
                x1, x2 = y  # x2 == possition , x3 == velocity
                err = u - x1
                funcErr = func.evalFunction(err, finalString)
                dydt = [x2, (-B * x2 - k * x1 + funcErr) / M]
                return dydt

            sol = odeint(ode, y0, t)

            controlingEffort = []

            for i in sol[:, 0]:
                error = u - i
                funcError = func.evalFunction(error, finalString)
                controlingEffort.append(funcError)

            secondCost = 0
            integralArray = []
            for i in sol[:, 0]:
                integralArray.append(abs(1.0 - i))

            # firstCost = np.trapz(abs(controlingEffort))
            secondCost = 0
            for i in integralArray:
                secondCost = secondCost + i / len(integralArray)

            firstCost = 0
            for i in controlingEffort:
                firstCost = firstCost + abs(i) / len(controlingEffort)

            vibration = 0
            vibPos = False
            invalidVib = True
            for i in sol[:, 0]:
                if vibPos == False:
                    if i > 1.02:
                        vibPos = True
                        vibration = vibration + 1
                elif vibPos:
                    if i < 0.98:
                        vibPos = False
                        vibration = vibration + 1
                if abs(i - 1) < 0.02:
                    invalidVib = False

            counter = 0
            for i in sol[:, 0]:
                counter = counter + 1
                if counter > 4000:
                    if i < 0.25:
                        secondCost = 10000
                        break

            thirdCost = 0
            if invalidVib:
                thirdCost = 10000
            else:
                thirdCost = vibration

            result = firstCost + 5000 * secondCost + thirdCost

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
    final, funn = mainCost(position)
    try:
        x0 = sp.symbols("x0")
        # np.tanh = sp.symbols("np.tanh")
        result1 = eval(funn)
        # result1 = sp.simplify(eval(funn))
    except:
        result1 = str(funn)
    result = str(result1)
    return result

# pp = [-1, -1, 0, -1, 0, 0, -1, 0, 0, 0, -1, 0, 0, -1, -1, 0, -1, 0, 0, -1, -1, -1, -1, -1, 0, 0, -1, 0, 0, -1, -1, -1, -1, -1, 0, -1, -1, -1, 0, -1, 0, -1, -1, 0, -1, -1, -1, -1, -1, 0, 0, -1, 0, -1, -1, -1, 0, -1, 0, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 0, 0, -1, 0, -1, -1, -1, 0, -1, 0, 0, -1, 0, -1, -1, -1, -1, -1, 0, 0, -1, 0, -1, -1, -1, -1, -1, -1, 0, -1, 0, -1, 0, 0, -1, -1, -1, -1, 0, 0, -1, 0, -1, -1, 0, 0, -1, 0, -1, -1, 0, 0, -1, 0, -1, 0, 0, -1, 0, -1, 0, -1, 0, -1, 0, 0, -1, -1, -1, -1, 0, -1, -1, 0, -1, -1, -1, 0, 0, 0]
# #
# print(str(costNumber(pp)))
# print(str(bestFunc(pp)))

# x = sp.symbols("x")
#
# x = 2
# h = eval('4*x')
# print(h)
# print(func.sigmoid(5.6))
# print((np.tan(7 - np.cos(8))))
