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


import parameters as par
import functions as func


def stringFuncGenerator(position, funcLib, operators, realNum):
    finalString = []
    firstNumberString = []
    secondNumberString = []
    functionString = []
    firstOperatorString = []
    secondOperatorString = []

    firstNumberCount = par.firstNumCount
    seconddNumberCount = par.seconNumCount
    functionCount = par.functionNum
    firstOperatorCount = par.firstOperationNum
    secondOperatorCount = par.seconOperationNum

    for i in position[:firstNumberCount]:
        firstNumberString += realNum[i]
    for i in position[firstNumberCount:firstNumberCount + seconddNumberCount]:
        secondNumberString += realNum[i]
    for i in position[firstNumberCount + seconddNumberCount:firstNumberCount + seconddNumberCount + functionCount]:
        functionString += funcLib[i]
    newStart = firstNumberCount + seconddNumberCount + functionCount
    for i in position[newStart:newStart + firstOperatorCount]:
        firstOperatorString += operators[i]
    for i in position[newStart + firstOperatorCount:newStart + firstOperatorCount + secondOperatorCount]:
        secondOperatorString += operators[i]

    finalString = firstNumberString + firstOperatorString + functionString + secondOperatorString + secondNumberString
    return finalString


funcLib = ['sp.sin(x0)', 'sp.cos(x0)', 'sp.tan(x0)', 'sp.cot(x0)', 'sp.exp(x0)', 'sp.sqrt(x0)', 'x0']
operators = ['*', '/', '+', '-', '**']
realNum = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
position = []
# k, a, b, c = normalizeLength(funcLib, operators, realNum)
nothing = ['']
k, newF, newO, newR = func.normalizeLength(funcLib, operators, realNum)  # funcLib + 4 * nothing
# newO = operators * 2 + nothing
# newR = realNum
for i in range(k * 5):
    position.append(i)
b = stringFuncGenerator(position, newF, newO, newR)
print(b)
