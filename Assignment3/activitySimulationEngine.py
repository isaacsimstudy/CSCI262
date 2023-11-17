import random
def generateEvents(eventName, eventType, eventMin, eventMax, statMean, statSD, days):
    event = [[eventName[j]] + [0 for i in range(days)] for j in range(len(eventName))]
    contZScore = generateZScore(3000, days)
    disZScore = generateZScore(1000, days)
    for i in range(len(eventName)):
        for j in range(2, days):
            if eventType[i] == "C":
                #Function to generate continuous data
                event[i][j] = round(generateBaselineData(contZScore[j], statMean[i], statSD[i], eventMin[i], eventMax[i]),2)
            else:
                #Function to generate discrete data
                event[i][j] = int(generateBaselineData(disZScore[j], statMean[i], statSD[i], eventMin[i], eventMax[i]))
    return event

def generateBaselineData(zScore, statMean, statSD, eventMin, eventMax):
    while True:
        event = (zScore * float(statSD)) + float(statMean)
        if float(eventMin) < event < float(eventMax):
            return event

def generateZScore(CD, days):
    day = []
    for i in range(days):
        day.append(random.randint(0, CD))

    mean = sum(day) / len(day)

    sd = 0
    for i in range(len(day)):
        sd = sd + (day[i] - mean) ** 2
    sd = (sd / days) ** 0.5

    zScore = []
    for i in range(len(day)):
        zScore.append((day[i] - mean) / sd)
    return zScore