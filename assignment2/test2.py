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

# Example usage:
K = 8  # Number of bits
M = 1  # Number of subpuzzles
H = 256  # Total number of guesses
print(count_distributions(K, M, H))
