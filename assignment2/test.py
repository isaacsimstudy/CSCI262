from itertools import product

def count_distributions(K, M, H):

    # Generate all possible K-bit binary numbers
    all_guesses = [''.join(i) for i in product('01', repeat=K)]
    
    # Convert binary strings to their corresponding guess count
    guess_values = [int(b, 2) + 1 for b in all_guesses]

    # Generate all possible distributions of guesses
    all_combinations = list(product(guess_values, repeat=M))
    
    # Filter combinations that sum up to H
    valid_combinations = [comb for comb in all_combinations if sum(comb) == H]
    
    # Return the count of valid distributions
    return len(valid_combinations)

# Example usage:
K = 2  # Number of bits
M = 4  # Number of subpuzzles
H = 9  # Total number of guesses

# Call the function with the example values
print(count_distributions(K, M, H))
