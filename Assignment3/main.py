from analysisEngine import analyseData, logNewData, getZScoreDayEvent
from alertEngine import flagAlerts, getthreshHold
from input import takeInput, readEventFile, checkEventNames, checkNumEvents, readStatsFiles
from activitySimulationEngine import generateEvents, logEvents

def main():
    #Tracking inputs taken
    hasTakenInput = 0
    print("Checking input for event file, stats file and number of days")
    #Taking Input
    event_file, stats_file, days, hasTakenInput = takeInput(hasTakenInput)

    #Reading Files
    eventName, eventType, eventMin, eventMax, eventWeight = readEventFile(event_file)
    statName, statMean, statSD = readStatsFiles(stats_file)
    checkEventNames(eventName, statName)
    checkNumEvents(eventName, statName)

    #Activity Simulation
    print("\nGenerating and logging events")
    events = generateEvents(eventName, eventType, eventMin, eventMax, statMean, statSD, days)

    #Logging events
    logEvents(events, days, hasTakenInput - 1)

    #Analyse data
    threshHoldMean, threshHoldSD, meanZSCORE = analyseData(events, days)

    logNewData(eventName, threshHoldMean, threshHoldSD, hasTakenInput - 1)

    sumWeight = getthreshHold(meanZSCORE, eventWeight)

    #Alerting
    #Continue taking input until stopped
    while True:
        print("\n----------------------------------------")
        print("Enter new stat file and days")
        stats_file, days, hasTakenInput = takeInput(hasTakenInput)

        newStatName, newStatMean, newStatSD = readStatsFiles(stats_file)

        newEvents = generateEvents(eventName, eventType, eventMin, eventMax, newStatMean, newStatSD, days)

        logEvents(newEvents, days, hasTakenInput)

        dayZScore = getZScoreDayEvent(newEvents, days, threshHoldMean, threshHoldSD)

        print("\n----------------------------------------")
        print(f"Threshold: {sumWeight}")
        print("----------------------------------------")
        print("Alerts")
        flagAlerts(dayZScore, sumWeight, eventName, days)
        print("----------------------------------------")
        print("Done")
        while True:
            print("Do you want to continue? (y/n)")
            choice = input()
            if choice == "y":
                break
            elif choice == "n":
                exit()
            else:
                print("Invalid input")
                continue


if __name__ == "__main__":
    main()
