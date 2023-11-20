import numpy as np
def flagAlerts(dayZScore, thresHold, eventName, days):
    sumofDay = 0
    counter = 0
    for i in range(days):
        for j in range(len(eventName)):
            sumofDay = sumofDay + dayZScore[j][i]
        if sumofDay > thresHold:
            print(f"Day {i + 1} is flagged")
            counter += 1
        sumofDay = 0
    print(f"Total number of days flagged: {counter}")

def getthreshHold(meanZScore, weight):
    totalweight = 0.00
    for i in range(len(meanZScore)):
        totalweight = totalweight + (meanZScore[i] * np.float64(weight[i]))
    return 2 * totalweight