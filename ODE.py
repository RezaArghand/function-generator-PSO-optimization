import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import functions as func

M = 1
B = 10
k = 20
u = 1
t = np.linspace(0, 5, 20000)
mengaT = np.linspace(0, 5, 500)
y0 = [0, 0]


def solveAndPlot(sstring):
    finalString = sstring

    def ode(y, t):
        x2, x3 = y  # x2 == possition , x3 == velocity
        error = u - x2
        funcError = func.evalFunction(error, finalString)
        dydt = [x3, (-B * x3 - k * x2 + funcError) / M]
        return dydt

    mengaFunc = 'np.tanh(np.tanh(np.tanh(np.tanh(x0)*81.6497)*8)*abs(np.sqrt(np.pi)* np.log(6)))*np.pi*81.6497'

    def odeMenga(y, t):
        x2, x3 = y  # x2 == possition , x3 == velocity
        error = u - x2
        funcError = func.evalFunction(error, mengaFunc)
        dydt = [x3, (-B * x3 - k * x2 + funcError) / M]
        return dydt

    sol = odeint(ode, y0, t)

    solMenga = odeint(odeMenga, y0, t)
    controlingEffort = []
    mengaControlingEffort = []
    for i in sol[:, 0]:
        error = u - i
        funcError = func.evalFunction(error, finalString)
        controlingEffort.append(funcError)

    for i in solMenga[:, 0]:
        errorMenga = u - i
        funcErrorMenga = func.evalFunction(errorMenga, mengaFunc)
        mengaControlingEffort.append(funcErrorMenga)
    firstCost = 0
    for i in controlingEffort:
        firstCost = firstCost + abs(i) / len(controlingEffort)

    firstCostMenga = 0
    for i in mengaControlingEffort:
        firstCostMenga = firstCostMenga + abs(i) / len(mengaControlingEffort)

    integralArray = []
    for i in sol[:, 0]:
        integralArray.append(abs(1.0 - i))

    integralArrayMenga = []
    for i in solMenga[:, 0]:
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
    thirdCost = 0
    if invalidVib:
        thirdCost = 10000
    else:
        thirdCost = vibration

    vibrationMenga = 0
    vibPosMenga = False
    for i in solMenga[:, 0]:
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

    mengaFullCost = secondCostMenga + thirdCostMenga
    resultFullCost = secondCost + thirdCost

    print('menga cost: ' + str(secondCostMenga))
    print('result cost: ' + str(secondCost))
    print('..........................................')
    print('menga controlling effort cost: ' + str(firstCostMenga))
    print('result controlling effort cost: ' + str(firstCost))
    print('..........................................')
    print('menga vibration cost: ' + str(thirdCostMenga))
    print('result vibration cost: ' + str(thirdCost))
    print('..........................................')
    print('menga final cost: ' + str(mengaFullCost))
    print('result final cost: ' + str(resultFullCost))

    plt.plot(t, sol[:, 0], 'b', label='x(t) - rasa')
    plt.plot(t, solMenga[:, 0], 'g', label='x(t) - manga')
    plt.title(finalString)
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.ylabel('X')
    plt.grid()
    # plt.show()
    plt.savefig("0001plot_Position.png")
    plt.close()

    plt.plot(t, sol[:, 1], 'b', label='x(t) - rasa')
    plt.plot(t, solMenga[:, 1], 'g', label='x(t) - manga')
    plt.title(finalString)
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.ylabel('X')
    plt.grid()
    plt.savefig("001plot_Velocity.png")
    plt.close()

    plt.plot(t, controlingEffort, 'b', label='x(t) - rasa')
    plt.plot(t, mengaControlingEffort, 'g', label='x(t) - manga')
    plt.title(finalString)
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.ylabel('X')
    plt.grid()
    plt.savefig("01plot_CotrollingEffort.png")
    plt.close()


# menga = 'np.tanh(np.tanh(np.tanh(np.tanh(x0)*81.6497)*8)*abs(np.sqrt(np.pi)* np.log(6)))*np.pi*81.6497'
rasa = 'np.floor(x0*334.5164)'
# solveAndPlot(rasa)
