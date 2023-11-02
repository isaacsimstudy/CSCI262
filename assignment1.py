import hashlib

def hashPassword(firstPassword):
    for i in range(5):
        if(i == 0):
            hashedPassword = hashlib.md5(firstPassword.encode()).hexdigest()
            hashedPassword = int(hashedPassword, 16)
            reducedPassword = (hashedPassword) % count
            marked[reducedPassword] = 1
        else:
            hashedPassword = hashlib.md5(passwords[reducedPassword].encode()).hexdigest()
            decHashedPassword = int(hashedPassword, 16)
            reducedPassword = decHashedPassword % count
            marked[reducedPassword] = 1
            if (i == 4):
                rainbowTable.append([firstPassword, hashedPassword])

count = 0
with open('password.txt', 'r') as file:
    passwords = file.readlines()
    count = len(passwords)

print("Total Passwords read: " + str(count))

marked = [0] * count
rainbowTable = []

for password in range(len(passwords)):
    if marked[password] == 1:
        continue
    else:
        hashPassword(passwords[password].strip('\n'))

print("All passwords hashed and stored in rainbow table.")
sortedRainbowTable = sorted(rainbowTable, key=lambda x: x[1])
with open('Rainbow.txt', 'w') as file:
    for i in range(len(sortedRainbowTable)):
        file.write(str(sortedRainbowTable[i]) + "\n")
    print(len(sortedRainbowTable))
    file.close()

inputHash = input("Enter hash to search: ")

