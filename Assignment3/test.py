import random
days = 30

eventName = ["A", "B", "C", "D", "E"]
event = [[0 for i in range(days)] for j in range(len(eventName))]
for i in range(len(eventName)):
    for j in range(days):
        event[i][j] = random.randint(0, 100)
print(event)