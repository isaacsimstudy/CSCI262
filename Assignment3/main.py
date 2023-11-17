from input import *
from activitySimulationEngine import *

def main():
    print("Taking input for event file, stats file and number of days")
    #Taking Input
    event_file, stats_file, days = takeInput()

    #Reading Files
    eventName, eventType, eventMin, eventMax, eventWeight, statName, statMean, statSD = readFiles(event_file, stats_file)

    #Generating and logging events
    print("\n")
    print("Generating and logging events")
    events = generateEvents(eventName, eventType, eventMin, eventMax, statMean, statSD, days)

    print(events)
    #2D List that will serve as header to events
    header = [["Event Name"] + [f"Days {i}" for i in range(days)]]
    for i in range(len(events)):
        header.append(events[i])
    print("\n")
    print("Writing to csv")
    with open('events.csv', 'w') as file:
        for i in range(len(header)):
            file.write(str(header[i]) + "\n")
        file.close()

if __name__ == "__main__":
    main()
