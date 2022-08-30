from logging import exception
import math
import random
from turtle import goto
import numpy as np
import parameters as par
import sympy as sp
import functions as func
from scipy.stats import logistic
import time
import multiprocessing
from scipy.integrate import odeint
from scipy.integrate import solve_ivp


# x_0 = sp.symbols("x_0") # position
# x_1 = sp.symbols("x_1") # velocity
# x_2 = sp.symbols("x_2") # integral


def mainCost(position):
    
    library = par.finalLib
    theString = []
    realNumberLib = []
    funcLib = []
    for i in range(15, 30):  # function and numbers order list
        realNum = func.map_value(position[i], par.min_of_variable, par.max_of_variable,
            -par.bound_of_realNumber, par.bound_of_realNumber)
        theNum = round(realNum, 2)
        mappedNumber = str(theNum)
        realNumberLib.append(mappedNumber)

    for i in range(0, 15):
        pos = int(np.floor(abs(position[i])))
        funcLib.append(library[pos])

    mainLib = funcLib + realNumberLib  # create main lib of functions and numbers
    tempOrderList = []
    for i in range(30, 60):
        tempOrderList.append(position[i])
    sortedList = func.mamalSorting(tempOrderList)
    for i in sortedList:
        theString.append(mainLib[i])

    primaryString = "".join(theString)
    finalString = func.makeBalanced(primaryString)
    
    # # reading all functions to decide about them
    # f = open("allStrings.txt", "r+")
    # content = f.read()
    # newContent=("\n string => %s "% (str(finalString)))
    # f.seek(0)
    # finalContent = newContent + content
    # f.write(finalContent)
    # f.close()    

    if func.isDevidableByZero(finalString) and ('x_2' in finalString or 'x_0' in finalString or 'x_1' in finalString):
        try:
            
            # if 'x0' in theString:
            #     theString += ''
            # else:
            #     theString += '-x0*5000'
            result=100000.0  # initiate cost function
            # ODE solution start ////////////////////////////////////////////////////////////////////////////////
            M = 1.0
            B = 10.0
            k = 20.0
            u = 1.0
            t_eval = np.arange(0, 3.0001, 0.0001)
            def ode(y, t):
                errr=1-y[0]
                funcError = func.evalFunction(errr, y[1], y[2], finalString)
                yd_0 = y[1]
                yd_1 = (-B * y[1] - k * y[0] + funcError) / M
                yd_2 = 1-y[0]
                return [yd_0, yd_1, yd_2]
            
            tStart=time.time()
            sol = odeint(ode,[0,0,0] , t_eval)
            tend=time.time()

            
            solutionSize=len(sol[:,1])
            controlingEffort = []

            for i in range(solutionSize):
                
                error = u - sol[i,0]
                velocity=sol[i,1]
                integral=sol[i,2]
                funcError = func.evalFunction(error, velocity, integral, finalString)
                controlingEffort.append(funcError)

            secondCost = 0
            integralArray = []
            for i in sol[:, 0]:
                integralArray.append(abs(u - i))

            # firstCost = np.trapz(abs(controlingEffort))
            secondCost = 0
            for i in integralArray:
                secondCost = secondCost + i / len(integralArray)

            firstCost = 0
            for i in controlingEffort:
                firstCost = firstCost + abs(i) / len(controlingEffort)

            

            

            position_cost=secondCost
            effort_cost=firstCost            
            maxOfControllingEffort=max(max(controlingEffort),abs(min(controlingEffort)))
            # result = (10 * position_cost + 0.01 * effort_cost + 0.05 * maxOfControllingEffort)
            result = position_cost
            mainFunc = finalString  # eval(finalString)
                
            if(tend-tStart>10.0):
                
                f = open("badFunctions.txt", "r+")

                newContent=("\n time => %s \n function => %s " % (
                    str(tend-tStart), str(mainFunc)))
                content = f.read()
                f.seek(0)
                finalContent = newContent + content
                f.write(finalContent)
                f.close()

            
        except Exception as e:
            result = 10000.0
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
        x_0 = sp.symbols("x_0")
        x_1 = sp.symbols('x_1')
        x_2 = sp.symbols('x_2')
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

# print(h)
# print(func.sigmoid(5.6))
# print((np.tan(7 - np.cos(8))))
