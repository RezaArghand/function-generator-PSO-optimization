            def F(y, t):
                x1,x2,x3=y
                # x2 == possition , x3 == velocity
                err = u - x1
                funcErr = func.evalFunction(err, x2, x3, finalString)
                dydt = [x1,x2, (-B * x2 - k * x1 + funcErr) / M]
                return dydt
            
            tStart=time.time()
            sol = odeint(F,[0,0,0] , t_eval)
            tend=time.time()
            
            
            controlingEffort = []

            for i in sol[:, 0]:
                error = u - i
                funcError = func.evalFunction(error, finalString)
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

            counter = 0
            for i in sol[:, 0]:
                counter = counter + 1
                if counter > 18000:
                    if i < 0.25:
                        secondCost = 10000
                        break

            thirdCost = 0
            if invalidVib:
                thirdCost = 10000
            else:
                thirdCost = vibration

            position_cost=secondCost
            effort_cost=firstCost            
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
