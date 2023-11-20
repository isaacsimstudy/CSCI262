from input import *
from activitySimulationEngine import *

def main():
    print("Taking input for event file, stats file and number of days")
    #Taking Input
    event_file, stats_file, days = takeInput()

    #Reading Files
    eventName, eventType, eventMin, eventMax, eventWeight, statName, statMean, statSD = readFiles(event_file, stats_file)

    print("Generating and logging events")
    events = generateEvents(eventName, eventType, eventMin, eventMax, statMean, statSD, days)

    #Logging events
    logEvents(events, days)


if __name__ == "__main__":
    main()
