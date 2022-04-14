import math
import random
import numpy as np
import parameters as par
import sympy as sp
import functions as func
from scipy.stats import logistic
import combinations_15 as mengaArray

x0 = sp.symbols("x0")


def mainCost(position):
    comb = par.combinationList
    theString = []
    realNumberLib = []
    combPos = int(np.floor(abs(position[0])))
    choosenList = comb[combPos]
    for i in range(1, len(position)):  # function and numbers order list
        realNum = func.map_value(position[i], par.min_of_variable, par.max_of_variable,
                                 -par.bound_of_realNumber,
                                 par.bound_of_realNumber)
        theNum = round(realNum, 2)
        mappedNumber = ' + ' + str(theNum)
        realNumberLib.append(mappedNumber)

    mainLib = par.finalLib + realNumberLib  # create main lib of functions and numbers

    for i in choosenList:
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
            t = np.linspace(-10, 10, 1000)
            mengaX = []
            resultX = []
            mengaString = 'np.tanh(np.tanh(np.tanh(np.tanh(x0)*81.6497)*8)*abs(np.sqrt(np.pi)* np.log(6)))*np.pi*81.6497'
            # mengaString='3.4 * x0'
            for i in t:
                menga = func.evalFunction(i, mengaString)
                funResult = func.evalFunction(i, finalString)
                mengaX.append(menga)
                resultX.append(funResult)
            finalArray = []
            for i in range(len(t)):
                finalArray.append(abs(mengaX[i] - resultX[i]))
            result = 0
            for i in finalArray:
                result = result + i / len(finalArray)

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
