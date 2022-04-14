import math
import random
import numpy as np
import parameters as par
import sympy as sp
import functions as func
from scipy.stats import logistic
import mengaX as mengaArray

x0 = sp.symbols("x0")


def mainCost(position):
    theString = []
    StringLib = []
    realNumberLib = []
    for i in range(0, 2* int(len(position) / 3)): # function and numbers order list
        StringLib.append(position[i])

    for i in range(int(2 * len(position) / 3), len(position)): # numbers strings
        realNum = func.map_value(100 * position[i], 100 * par.min_of_variable, 100 * par.max_of_variable, -par.bound_of_realNumber,
                                 par.bound_of_realNumber)
        theNum=round(realNum,2)
        mappedNumber = '+ ' + str(theNum)+' *'
        realNumberLib.append(mappedNumber)

    mainLib = par.finalLib + realNumberLib # create main lib of functions and numbers

    sortedListFunctions = func.mamalSorting(StringLib)   # sorted array

    for i in sortedListFunctions:   # building the function based on the order
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
            t = np.linspace(-10, 10, 5000)
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
        result1 = sp.simplify(eval(funn))
    except:
        result1 = str(funn)
    result = str(result1)
    return result

# pp = [1, 5, 0, 0, 0, 0, 0]
# #
# print(str(costNumber(pp)))
# print(str(bestFunc(pp)))

# x = sp.symbols("x")
#
# x = 2
# h = eval('4*x')
# print(h)
# print(func.sigmoid(5.6))
# print(sp.N(sp.tan(7 - sp.cos(8))))
