import numpy as np
def getMeanSD(events, mean, sd):
    for i in range(len(events)):
        mean.append(np.mean(events[i][1:]))
        sd.append(np.std(events[i][1:]))
    return mean, sd

def getZScoreDayEvent(events, days, mean, sd):
    zScore = []
    for i in range(len(events)):
        zScoreDay = []
        for j in range(1, days + 1):
            #New list that will be appended to zScore later
            zScoreDay.append(abs((events[i][j] - mean[i]) / sd[i]))
        zScore.append(zScoreDay)
    return zScore

def getMeanZScore(zScore, events):
    meanZScore = []
    for i in range(len(events)):
        meanZScore.append(np.mean(zScore[i]))
        print(f"Mean Z score for {events[i][0]}: {meanZScore[i]}")
    return meanZScore
def analyseData(events, days):
    #From events list, calculate the mean and SD for each event
    #For each event, calculate the Z score for each day
    #For each event, calculate the mean of Z scores
    mean = []
    sd = []

    print("----------------------------------------")
    print(f"Calculating mean and SD for each event")
    mean, sd = getMeanSD(events, mean, sd)

    print("----------------------------------------")
    print(f"Calculating Z score for each day in each event")
    zScore = getZScoreDayEvent(events, days, mean, sd)
    print("----------------------------------------")

    print(f"Calculating mean Z score for each event")
    print("----------------------------------------")
    meanZScore = getMeanZScore(zScore, events)
    print("----------------------------------------")

    return mean, sd, meanZScore

def logNewData(eventName, newmean, newsd, hasTakenInput):
    print("\n----------------------------------------")
    print("Writing to file")
    if hasTakenInput == 0:
        fileName = "thresholdStats.txt"
    else:
        fileName = f"liveStats{hasTakenInput}.txt"
    with open(fileName, 'w') as file:
        file.write("Event Name, Mean, SD\n")
        for i in range(len(eventName)):
            file.write(f"{eventName[i]}, {newmean[i]}, {newsd[i]}\n")
    print("Done writing to file")
    print("----------------------------------------")