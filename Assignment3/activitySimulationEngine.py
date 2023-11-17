import random
def generateEvents(eventName, eventType, eventMin, eventMax, statMean, statSD, days):
    event = [[eventName[j]] + [0 for i in range(days)] for j in range(len(eventName))]
    contZScore = generateZScore(3000, days)
    disZScore = generateZScore(1000, days)
    for i in range(len(eventName)):
        print(len(event[i]))
        for j in range(1 ,days + 1):
            if eventType[i] == "C":
                #Function to generate continuous data
                event[i][j] = round(generateBaselineData(contZScore[j - 1], statMean[i], statSD[i], eventMin[i], eventMax[i]),2)
            else:
                #Function to generate discrete data
                event[i][j] = int(generateBaselineData(disZScore[j - 1], statMean[i], statSD[i], eventMin[i], eventMax[i]))
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

def logEvents(events, days):
    header = [["Event Name"] + [f"Days {i}" for i in range(1 , days + 1)]]
    for i in range(len(events)):
        header.append(events[i])
    print("\n")
    print("Writing to csv")
    with open('events.csv', 'w') as file:
        for i in range(len(header)):
            file.write(str(header[i]) + "\n")
        file.close()