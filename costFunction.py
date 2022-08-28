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


x_0 = sp.symbols("x_0") # position
x_1 = sp.symbols("x_1") # velocity
x_2 = sp.symbols("x_2") # integral


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

    if func.isDevidableByZero(finalString) and ('x_0' in finalString or 'x_2' in finalString or 'x_1' in finalString):
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
            t_eval = np.arange(0, 5.1, 0.1)
            terminationBios = 0.0

            # def ode(y, t):
            #     x1, x2 = y  # x1 == possition , x2 == velocity
            #     err = u - x1
            #     funcErr = func.evalFunction(err, x2, finalString)
            #     dydt = [x2, (-B * x2 - k * x1 + funcErr) / M]
            #     return dydt
            
            # sol = odeint(ode, y0, t)
            
            ####
            # solving ODE in new method
            ####
            def F(t, y):
                # y[0] = possition
                # y[1] = velocity
                # y[2] = integral of position
                errorr = u - y[0]
                funcError = func.evalFunction(errorr, y[1], y[2], finalString)

                yd_0 = y[1]
                yd_1 = (-B * y[1] - k * y[0] + funcError)/ M
                yd_2 = 1 - y[0]

                return [yd_0, yd_1, yd_2]
            
            def runODE():
                kkk = solve_ivp(F, [0, 5], [0.0, 0.0, 0.0], t_eval=t_eval)
                return kkk
            
            if __name__ == '__main__':
                # "Starting" myFunction as a process
                p = multiprocessing.Process(target=runODE)
                p.start()

                # Waits for 10 seconds or until the function execution is over
                p.join(10)

                # If the process "p" is still alive
                if p.is_alive():

                    # The process is terminated
                    p.terminate()
                    p.join()
                    
                    terminationBios = 100000
                
            
            
            if terminationBios==0.0:
                tStart=time.time()
                sol = solve_ivp(F, [0, 5], [0.0, 0.0, 0.0], t_eval=t_eval)
                tend=time.time()
                controlingEffort = []

                for i in range(len(sol.y.T[:, 0])):
                    error = u - sol.y.T[i][0]
                    xDot = sol.y.T[i][1]
                    xIntegral=sol.y.T[i][2]
                    funcError = func.evalFunction(error, xDot, xIntegral, finalString)
                    controlingEffort.append(funcError)

            
                integralArray = []
                for i in sol.y.T[:, 0]:
                    integralArray.append(abs(u - i))

                # firstCost = np.trapz(abs(controlingEffort))
                secondCost = 0  # main cost calculation
                for i in integralArray:
                    secondCost = secondCost + i / len(integralArray)
                

                firstCost = 0  # controlling effort calculation
                for i in controlingEffort:
                    firstCost = firstCost + abs(i) / len(controlingEffort)

                vibration = 0
                vibPos = False
                invalidVib = True
                for i in sol.y.T[:, 0]:
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
                for i in sol.y.T[:, 0]:
                    counter = counter + 1
                    if counter > 18000:
                        if i < 0.25:
                            secondCost = 10000
                            break
                position_cost=secondCost
                effort_cost=firstCost                    
                thirdCost = 0
                if invalidVib:
                    thirdCost = 10000
                else:
                    thirdCost = vibration

                maxOfControllingEffort=max(max(controlingEffort),abs(min(controlingEffort)))
                result = (10 * position_cost + 0.01 * effort_cost + 0.05 * maxOfControllingEffort)
                # result = 100 * position_cost
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
            else:
                result = 12500
                print('terminal bios accured////////////////////////////////////////////////////////////////////////')
        except:
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
