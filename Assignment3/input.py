import os
import sys
def takeInput():
    if len(sys.argv) == 4:
        eventFileName = sys.argv[1]
        statFileName = sys.argv[2]
        days = sys.argv[3]
    #Take input for event file, stat file and number of days, if event file or stat file does not exist, ask again
    event = True
    stat = True
    while event:
        if os.path.exists(eventFileName):
            event = False
        else:
            print("Error: Event file does not exist")
            eventFileName = input("Re-Enter event file name: ")

    while stat:
        if os.path.exists(statFileName):
            stat = False
        else:
            print("Error: Stats file does not exist")
            statFileName = input("Re-Enter stats file name: ")

    while True:
        #Check if days is not a number or 0
        try:
            days = int(days)
            if days <= 0:
                print("Error: Days cannot be 0 or negative")
                days = input("Re-Enter number of days: ")
            else:
                break
        except ValueError:
            print("Error: Days is not a number")
            days = input("Re-Enter number of days: ")

    return eventFileName, statFileName, days

def readFiles(event_file, stats_file):
    eventNames = []
    eventTypes = []
    eventMinimum = []
    eventMaximum = []
    eventWeights = []
    statNames = []
    statMeans = []
    statSDs = []
    #Read event file and stats file
    with open(event_file, "r") as event_file:
        allevents = event_file.readlines()

    with open(stats_file, "r") as stats_file:
        allstats = stats_file.readlines()


    checkNumEvents(allevents, allstats)

    for i in range(len(allevents)):
        eventNames.append(allevents[i].split(':')[0])
        eventTypes.append(allevents[i].split(':')[1])
        eventMinimum.append(allevents[i].split(':')[2])
        eventMaximum.append(allevents[i].split(':')[3])
        eventWeights.append(allevents[i].split(':')[4])
        if eventNames == "":
            print("Error: Event name is empty")
            eventNames = input(f"Enter event name for {i} row: ")
        if eventTypes == "":
            print("Error: Event type is empty")
            eventTypes = input(f"Enter event type for {eventNames[i]} row: ")
        if eventMinimum == "":
            print("Error: Event minimum is empty")
            eventMinimum = input(f"Enter event minimum for {eventNames[i]} row: ")
        if eventMaximum == "":
            print("Error: Event maximum is empty")
            eventMaximum = input(f"Enter event maximum for {eventNames[i]} row: ")
        if eventWeights == "":
            print("Error: Event weight is empty")
            eventWeights = input(f"Enter event weight for {eventNames[i]} row: ")
        print(f"This is the {i + 1} row of event file: {eventNames[i]}: {eventTypes[i]} : {eventMinimum[i]} : {eventMaximum[i]} : {eventWeights[i]} ")

    print("\n")
    for j in range(len(allstats)):
        statNames.append(allstats[j].split(':')[0])
        statMeans.append(allstats[j].split(':')[1])
        statSDs.append(allstats[j].split(':')[2])
        if statNames == "":
            print("Error: Stat name is empty")
            statNames = input(f"Enter stat name for {j} row: ")
        if statMeans == "":
            print("Error: Stat mean is empty")
            statMeans = input(f"Enter stat mean for {statNames[j]} row: ")
        if statSDs == "":
            print("Error: Stat SD is empty")
            statSDs = input(f"Enter stat SD for {statNames[j]} row: ")
        print(f"This is the {j + 1} row of stats file: {statNames[j]}: {statMeans[j]} : {statSDs[j]} ")

    checkEventNames(allevents, allstats)

    return eventNames, eventTypes, eventMinimum, eventMaximum, eventWeights, statNames, statMeans, statSDs

def checkNumEvents(events, stats):
    #Check if number of events in event file and stats file are same
    print("Checking if number of events in event file and stats file are same")
    if len(events) != len(stats):
        print("Error: Number of events in event file and stats file are not same")
        exit()

def checkEventNames(events, stats):
    #Check if event names in event file and stats file are same
    print("Checking if event names in event file and stats file are same")
    for i in range(len(events)):
        eventName = events[i].split(':')[0].lower()
        statName = stats[i].split(':')[0].lower()
        if eventName != statName:
            print("Error: Event names in event file and stats file are not same")
            exit()
    print("Ch")