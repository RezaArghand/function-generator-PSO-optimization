import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import functions as func
from scipy.integrate import solve_ivp
import sympy as sp

M = 1
B = 10
k = 20
u = 1
x_0 = sp.symbols("x_0")  # position
x_1 = sp.symbols("x_1")  # velocity
x_2 = sp.symbols("x_2")  # integral
t_eval = np.arange(0, 5.0001, 0.0001)




def solveAndPlot(sstring):
    finalString = sstring

    # def ode(y, t):
    #     x2, x3 = y  # x2 == possition , x3 == velocity
    #     error = u - x2
    #     newErr = u - x3
    #     funcError = func.evalFunction(error, newErr, finalString)
    #     dydt = [x3, (-B * x3 - k * x2 + funcError) / M]
    #     return dydt

    def F(t, y):
        # y[0] = possition
        # y[1] = velocity
        # y[2] = integral of position
        errorr = u - y[0]
        funcError = func.evalFunction(errorr, y[1], y[2], finalString)

        yd_0 = y[1]
        yd_1 = (-B * y[1] - k * y[0] + funcError) / M
        yd_2 = 1-y[0]

        return [yd_0, yd_1, yd_2]


    sol = solve_ivp(F, [0, 5], [0.0, 0.0, 0.0], t_eval=t_eval)

    mengaFunc = 'np.tanh(np.tanh(np.tanh(np.tanh(x_0)*81.6497)*8)*abs(np.sqrt(np.pi)* np.log(6)))*np.pi*81.6497'

    def F_Menga(t, y):
        # y[0] = possition
        # y[1] = velocity
        # y[2] = integral of position
        errorr = u - y[0]
        funcError = func.evalFunction(errorr, y[1], y[2], mengaFunc)

        yd_0 = y[1]
        yd_1 = (-B * y[1] - k * y[0] + funcError) / M
        yd_2 = y[0]

        return [yd_0, yd_1, yd_2]

    solMenga = solve_ivp(F_Menga, [0, 5], [0.0, 0.0, 0.0], t_eval=t_eval)

    # def odeMenga(y, t):
    #     x2, x3 = y  # x2 == possition , x3 == velocity
    #     error = u - x2
    #     funcError = func.evalFunctionOneVariable(error, mengaFunc)
    #     dydt = [x3, (-B * x3 - k * x2 + funcError) / M]
    #     return dydt

    # # sol = odeint(ode, y0, t)

    # solMenga = odeint(odeMenga, y0, t)
    controlingEffort = []
    mengaControlingEffort = []
    for i in range(len(sol.y.T[:, 0])):
        error = u - sol.y.T[i][0]
        xDot = sol.y.T[i][1]
        xIntegral = sol.y.T[i][2]
        funcError = func.evalFunction(error, xDot, xIntegral, finalString)
        controlingEffort.append(funcError)

    for i in range(len(solMenga.y.T[:, 0])):
        error = u - solMenga.y.T[i][0]
        xDot = solMenga.y.T[i][1]
        xIntegral = solMenga.y.T[i][2]
        funcErrorMenga = func.evalFunction(error, xDot, xIntegral, mengaFunc)
        mengaControlingEffort.append(funcErrorMenga)

    firstCost = 0
    for i in controlingEffort:
        firstCost = firstCost + abs(i) / len(controlingEffort)

    firstCostMenga = 0
    for i in mengaControlingEffort:
        firstCostMenga = firstCostMenga + abs(i) / len(mengaControlingEffort)

    integralArray = []
    for i in sol.y.T[:, 0]:
        integralArray.append(abs(1.0 - i))

    integralArrayMenga = []
    for i in solMenga.y.T[:, 0]:
        integralArrayMenga.append(abs(1.0 - i))

    secondCost = 0
    for i in integralArray:
        secondCost = secondCost + i / len(integralArray)
    # firstCost = np.trapz(abs(controlingEffort))

    secondCostMenga = 0
    for i in integralArrayMenga:
        secondCostMenga = secondCostMenga + i / len(integralArrayMenga)

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
    thirdCost = 0
    if invalidVib:
        thirdCost = 10000
    else:
        thirdCost = vibration

    vibrationMenga = 0
    vibPosMenga = False
    for i in solMenga.y.T[:, 0]:
        if vibPosMenga == False:
            if i > 1.02:
                vibPosMenga = True
                vibrationMenga = vibrationMenga + 1
        elif vibPosMenga:
            if i < 0.98:
                vibPos = False
                vibrationMenga = vibrationMenga + 1
    thirdCostMenga = 0
    if vibrationMenga < 1:
        thirdCostMenga = 10000
    else:
        thirdCostMenga = vibrationMenga


    maxOfControllingEffortMenga = max(max(mengaControlingEffort), abs(min(mengaControlingEffort)))
    maxOfControllingEffort = max(max(controlingEffort), abs(min(controlingEffort)))
    mengaFullCost = 10 * (secondCostMenga + 0.001 * firstCostMenga + 0.01 * maxOfControllingEffortMenga)
    resultFullCost = 10 * (secondCost + 0.001 * firstCost + 0.01 * maxOfControllingEffort)
    print(np.size(t_eval))
    print(np.size(sol.y.T[:, 0]))
    print('menga cost: ' + str(secondCostMenga))
    print('result cost: ' + str(secondCost))
    print('..........................................')
    print('menga controlling effort cost: ' + str(firstCostMenga))
    print('result controlling effort cost: ' + str(firstCost))
    # print('..........................................')
    # print('menga vibration cost: ' + str(thirdCostMenga))
    # print('result vibration cost: ' + str(thirdCost))
    # print('..........................................')
    print('..........................................')
    print('menga max of controlling effort: ' + str(maxOfControllingEffortMenga))
    print('result max of controlling effort: ' + str(maxOfControllingEffort))
    print('..........................................')
    print('menga final cost: ' + str(mengaFullCost))
    print('rasa final cost: ' + str(resultFullCost))

    plt.plot(t_eval, sol.y.T[:, 0], 'b', label='x(t) - rasa')
    plt.plot(t_eval, solMenga.y.T[:, 0], 'g', label='x(t) - manga')
    plt.title(finalString)
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.ylabel('X')
    plt.grid()
    plt.show()
    plt.savefig("0001plot_Position.png")
    plt.close()

    plt.plot(t_eval, sol.y.T[:, 1], 'b', label='x(t) - rasa')
    plt.plot(t_eval, solMenga.y.T[:, 1], 'g', label='x(t) - manga')
    plt.title(finalString)
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.ylabel('X')
    plt.grid()
    plt.savefig("001plot_Velocity.png")
    plt.close()

    plt.plot(t_eval, controlingEffort, 'b', label='x(t) - rasa')
    plt.plot(t_eval, mengaControlingEffort, 'g', label='x(t) - manga')
    plt.title(finalString)
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.ylabel('X')
    plt.grid()
    plt.savefig("01plot_CotrollingEffort.png")
    plt.close()

# menga = 'np.tanh(np.tanh(np.tanh(np.tanh(x_0)*81.6497)*8)*abs(np.sqrt(np.pi)* np.log(6)))*np.pi*81.6497'
rasa = '2804.24*x_0 - 58.69*x_1/5755.05**x_2'
solveAndPlot(rasa)
'2804.24*x_0 - 58.69*x_1/5755.05**x_2'
'np.tan(-3432.14*np.sign(x_0 -2543.44))'