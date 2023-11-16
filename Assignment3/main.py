from input import *
def main():
    print("Taking input for event file, stats file and number of days")
    #Taking Input
    event_file, stats_file, days = takeInput()

    #Reading Files
    eventName, eventType, eventMin, eventMax, eventWeight, statName, statMean, statSD = readFiles(event_file, stats_file)

    #Generating and logging events
    print("\n")
    print("Generating and logging events")

if __name__ == "__main__":
    main()
