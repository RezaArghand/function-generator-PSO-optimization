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
        realN = str(round(newPosition[i], 2))
        theString.append('+')
        theString.append(mainList[position[i]])
        theString.append('+')
        theString.append(realN)
        theString.append(")")

    # finalString = "".join(func.makeBalanced(theString))
    sstring = "".join(theString)
    finalString = func.makeBalanced(sstring)
    mainFunc = finalString
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
                secondCost += abs(func.evalFunction(xx, finalString) - (np.sin(xx) ** 2 - 1.5))
            # secondCost = secondCost / steps
            result = secondCost
            # print(position)
            # result = firstCost

        except:
            result = 1000000
            mainFunc = finalString
    else:
        result = 1500000
        mainFunc = "there is no valid function"

    return result, mainFunc


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
            steps = 1000
            maxY = 100
            dx = maxY / steps
            secondCost = 0

            for i in range(0, steps):
                xx = dx * i
                secondCost += abs(func.evalFunction(xx, finalString) - np.sin(xx) * np.cos(xx))
            # secondCost = secondCost / steps
            result = secondCost
            # print(position)
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


# try:
#     # if 'x0' in theString:
#     #     theString += ''
#     # else:
#     #     theString += '-x0*5000'
#     finalString = func.makeBalanced(theString)
#     mainFunc = eval(finalString)
#     # print(mainFunc)
#     firstCost = abs(sp.N(mainFunc.subs(x0, 0)) - 1) + abs(sp.N(mainFunc.subs(x0, 5)) - 11)
#     # print(firstCost)
#     steps = 100
#     maxY = 5
#     dx = maxY / steps
#     secondCost = 0
#
#     for i in range(0, steps):
#         xx = dx * i
#         f1 = (sp.N(mainFunc.subs(x0, dx + xx)) - sp.N(mainFunc.subs(x0, xx))) ** 2
#         f2 = dx ** 2
#         f3 = np.sqrt(f1 + f2)
#         secondCost = secondCost + f3
#
#     result = (firstCost + abs(secondCost))
#
# except:
#     result = 1000
#     mainFunc = func.makeBalanced(theString)
#
# # old one
#
#
# import parameters as par
# import functions as func
#
#
# def stringFuncGenerator(position, funcLib, operators, realNum):
#     finalString = []
#     firstNumberString = []
#     secondNumberString = []
#     functionString = []
#     firstOperatorString = []
#     secondOperatorString = []
#
#     firstNumberCount = par.firstNumCount
#     seconddNumberCount = par.seconNumCount
#     functionCount = par.functionNum
#     firstOperatorCount = par.firstOperationNum
#     secondOperatorCount = par.seconOperationNum
#
#     for i in position[:firstNumberCount]:
#         firstNumberString += realNum[i]
#     for i in position[firstNumberCount:firstNumberCount + seconddNumberCount]:
#         secondNumberString += realNum[i]
#     for i in position[firstNumberCount + seconddNumberCount:firstNumberCount + seconddNumberCount + functionCount]:
#         functionString += funcLib[i]
#     newStart = firstNumberCount + seconddNumberCount + functionCount
#     for i in position[newStart:newStart + firstOperatorCount]:
#         firstOperatorString += operators[i]
#     for i in position[newStart + firstOperatorCount:newStart + firstOperatorCount + secondOperatorCount]:
#         secondOperatorString += operators[i]
#
#     finalString = firstNumberString + firstOperatorString + functionString + secondOperatorString + secondNumberString
#     return finalString
#
#
# funcLib = ['sp.sin(x0)', 'sp.cos(x0)', 'sp.tan(x0)', 'sp.cot(x0)', 'sp.exp(x0)', 'sp.sqrt(x0)', 'x0']
# operators = ['*', '/', '+', '-', '**']
# realNum = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
# position = []
# # k, a, b, c = normalizeLength(funcLib, operators, realNum)
# nothing = ['']
# k, newF, newO, newR = func.normalizeLength(funcLib, operators, realNum)  # funcLib + 4 * nothing
# # newO = operators * 2 + nothing
# # newR = realNum
# for i in range(k * 5):
#     position.append(i)
# b = stringFuncGenerator(position, newF, newO, newR)
# print(b)
