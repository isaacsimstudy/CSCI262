import csv

def count_distributions(K, M, H):
    # Base case: If we have no subpuzzles or no guesses, there's nothing to do
    if M == 0 or H == 0:
        return 0

    # Base case: With 1 subpuzzle, check if the remaining guesses form a valid binary number for K bits
    if M == 1:
        return 1 if 0 <= H-1 < 2**K else 0

    count = 0
    # Iterate through all possible guess values for a subpuzzle
    for guess in range(1, 2**K + 1):
        # Only proceed if the guess is less than or equal to the remaining guesses
        if guess <= H:
            # Recur for the remaining subpuzzles and guesses
            count += count_distributions(K, M-1, H-guess)
            
    return count


# While return of count_distributions is not 0, increment H
def find_min_guesses(K1, M1, K2, M2):
    Hash = 0
    distribution = []
    distribution.append(["Hashes", "Puzzle A Cases", "Puzzle B Cases"])
    x = 1
    y = 1
    while (x != 0 or y != 0 and Hash < K1 and Hash < K2):
        Hash += 1
        x = count_distributions(K1, M1, Hash)
        y = count_distributions(K2, M2, Hash)
        print("Hash: ", Hash, " x: ", x, " y: ", y)
        #Append to array with Hash and x and y
        if (x != 0 or y != 0):
            print(x, y)
            distribution.append([Hash, x, y])
    return distribution

K1 = int(input("Enter Puzzle A K1: "))
M1 = int(input("Enter Puzzle A M1: "))
K2 = int(input("Enter Puzzle B K2: "))
M2 = int(input("Enter Puzzle B M2: "))

array = find_min_guesses(K1, M1, K2, M2)
#Write to csv file
with open('q1.csv', 'w', newline='') as assignment2:
    csvWriter = csv.writer(assignment2)
    
    for row in array:
        csvWriter.writerow(row)
