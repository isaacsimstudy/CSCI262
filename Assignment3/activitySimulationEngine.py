import random
def generateEvents(eventName, eventType, eventMin, eventMax, statMean, statSD, days):
    event = [[eventName[j]] + [0 for i in range(days)] for j in range(len(eventName))]
    contZScore = generateZScore(3000, days)
    disZScore = generateZScore(1000, days)
    for i in range(len(eventName)):
        for j in range(1 ,days + 1):
            if eventType[i] == "C":
                #Function to generate continuous data
                event[i][j] = round(generateBaselineData(contZScore[j - 1], statMean[i], statSD[i], eventMin[i], eventMax[i]), 2)
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
    print("\n")
    print("Writing to file")
    with open("activities.txt", 'w') as file:
        #List 1 is the header where index 0 is "Event Name" and the rest are the days, for subsequent lists, the first element is the event name, the rest are the values
        for i in range(days):
            file.write(f"Event Name, Day {i + 1}\n")
            file.write(f"{events[0][0]}, {events[0][i + 1]}\n")
            file.write(f"{events[1][0]}, {events[1][i + 1]}\n")
            file.write(f"{events[2][0]}, {events[2][i + 1]}\n")
            file.write(f"{events[3][0]}, {events[3][i + 1]}\n")
            file.write(f"{events[4][0]}, {events[4][i + 1]}\n\n\n")
    print("Done writing to file")
    print("\n")
