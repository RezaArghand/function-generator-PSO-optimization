try:
    # if 'x0' in theString:
    #     theString += ''
    # else:
    #     theString += '-x0*5000'
    finalString = func.makeBalanced(theString)
    mainFunc = eval(finalString)
    # print(mainFunc)
    firstCost = abs(sp.N(mainFunc.subs(x0, 0)) - 1) + abs(sp.N(mainFunc.subs(x0, 5)) - 11)
    # print(firstCost)
    steps = 100
    maxY = 5
    dx = maxY / steps
    secondCost = 0

    for i in range(0, steps):
        xx = dx * i
        f1 = (sp.N(mainFunc.subs(x0, dx + xx)) - sp.N(mainFunc.subs(x0, xx))) ** 2
        f2 = dx ** 2
        f3 = np.sqrt(f1 + f2)
        secondCost = secondCost + f3

    result = (firstCost + abs(secondCost))

except:
    result = 1000
    mainFunc = func.makeBalanced(theString)

# old one


