import math
import random

import parameters as par


def RandomValidFunction():
    functionList = par.funcLib
    varNo = par.varNum
    minV = par.min_of_variable
    maxV = par.max_of_variable
    position = []
    run = True

    while run:
        for i in range(varNo):
            position += random.randint(minV, maxV)



