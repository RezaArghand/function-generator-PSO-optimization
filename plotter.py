import matplotlib.pyplot as plt
import numpy as np
import functions as func

t = np.linspace(0, 10, 1000)


def solveAndPlot(sstring):
    try:
        finalString = sstring
        mengaX = []
        resultX = []
        mengaString = 'np.tanh(np.tanh(np.tanh(np.tanh(x0)*81.6497)*8)*abs(np.sqrt(np.pi)* np.log(6)))*np.pi*81.6497'
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
        plt.close()
    except:
        print('plot error! ###########################################')

solveAndPlot('np.tanh(np.tanh(x0))+ 872.96+ -18.49+ -18.49+ -18.49+ -155.96+ -202.58+ -202.58')
