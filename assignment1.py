import hashlib

def hashPassword(firstPassword):
    for i in range(5):
        if(i == 0):
            hashedPassword = hashlib.md5(firstPassword.encode()).hexdigest()
            hashedPassword = int(hashedPassword, 16)
            reducedPassword = (hashedPassword) % count
            marked[reducedPassword] = 1
        else:
            hashedPassword = hashlib.md5(passwords[reducedPassword].strip('\n').encode()).hexdigest()
            decHashedPassword = int(hashedPassword, 16)
            reducedPassword = decHashedPassword % count
            marked[reducedPassword] = 1
            if (i == 4):
                endHash = hashlib.md5(passwords[reducedPassword].strip('\n').encode()).hexdigest()
                rainbowTable.append([firstPassword, endHash])
              
def reduceHash(rainbowPassword):
    for i in range(5):
        if(i == 0):
            hashedRainbowPassword = hashlib.md5(rainbowPassword.encode()).hexdigest()
            hashedRainbowPassword = int(hashedRainbowPassword, 16)
            reducedPassword = (hashedRainbowPassword) % count
        else:
            hashedPassword = hashlib.md5(passwords[reducedPassword].strip('\n').encode()).hexdigest()
            decHashedPassword = int(hashedPassword, 16)
            reducedPassword = decHashedPassword % count   
    return passwords[reducedPassword].strip('\n')

count = 0
with open('Passwords.txt', 'r') as file:
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
found = False

with open('Rainbow.txt', 'r') as file:
    rainbowTable = file.readlines()
    for i in range(len(rainbowTable)):
        rainbowTable[i] = rainbowTable[i].strip('\n')
    file.close()

#Check if input hash is in rainbow table
for i in range(len(rainbowTable)):
    if(rainbowTable[i].split(',')[1].strip(' \']') == inputHash):
        print("Hash found in rainbow table.")
        #Reduce hash to get password, since we know the password is the last one before the hash
        reducedPassword = rainbowTable[i].split(',')[0].strip('[\'')
        foundPassword = reduceHash(reducedPassword)
        hashFoundPassword = hashlib.md5(foundPassword.encode()).hexdigest()
        if (hashFoundPassword == inputHash):
            print("Password found: " + foundPassword)
            found = True
        break
    else:
        if(i == len(rainbowTable) - 1):
            print("Hash not found in rainbow table.")
        continue


if (found == False):
    for i in range(len(passwords)):
        if i == 0:
            decInputHash = int(inputHash, 16)
            reducedNumber = decInputHash % count
            reducedPassword = passwords[reducedNumber].strip('\n')
            hashReducedPassword = hashlib.md5(reducedPassword.encode()).hexdigest()
        else:
            decHashReducedPassword = int(hashReducedPassword, 16)
            reducedNumber = decHashReducedPassword % count
            reducedPassword = passwords[reducedNumber].strip('\n')
            hashReducedPassword = hashlib.md5(reducedPassword.encode()).hexdigest()
            print(reducedPassword)
        print(i)
        if(hashReducedPassword == inputHash):
            print("Password found: " + reducedPassword)
            break
        else:
            if(i == len(passwords) - 1):
                print("Password not found.")
            continue