import matplotlib.pyplot as plt
import numpy as np
import functions as func
import costFunction

t = np.linspace(-1, 1, 5000)


def solveAndPlot(sstring):
    try:
        finalString = sstring
        mengaX = []
        resultX = []
        mengaString = 'np.tanh(np.tanh(np.tanh(np.tanh(x0)*81.6497)*8)*abs(np.sqrt(np.pi)* np.log(6)))*np.pi*81.6497'
        # mengaString = '3.1*x0+12.6'
        for i in t:
            menga = func.evalFunction(i, mengaString)
            result = func.evalFunction(i, finalString)
            mengaX.append(menga)
            resultX.append(result)
        plt.plot(t, resultX, 'b', label='x(t) - rasa')
        plt.plot(t, mengaX, 'g', label='x(t) - manga')
        plt.title(finalString)
        plt.legend(loc='best')
        plt.xlabel('t')
        plt.ylabel('X')
        plt.grid()
        plt.savefig("01plot.png")
        plt.show()
        plt.close()
    except:
        print('error in plotting')


solveAndPlot('np.floor(41.0779*np.floor(x0))')
