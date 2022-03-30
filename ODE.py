import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import functions as func

M = 1
B = 10
k = 20
u = 1
kp = 20
t = np.linspace(0, 10, 100)

y0 = [0, 0]
finalString='x0*x0'
def ode(y, t):
    x2, x3 = y  #x2 == possition , x3 == velocity
    error= u-x2
    funcError = func.evalFunction(error, finalString)
    dydt = [x3, (-B*x3-k*x2+kp*funcError)/M]
    return dydt




sol =odeint(ode, y0, t)

plt.plot(t, sol[:, 0], 'b', label='x(t)')
plt.plot(t, sol[:, 1], 'g', label='v(t)')

plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()
