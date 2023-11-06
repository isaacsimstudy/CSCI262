from itertools import combinations_with_replacement

M = int(input("Enter the number of sub-puzzles to solve: "))
K = int(input("Enter the value of K: "))
H = int(input("Enter the value of H where H is number of hashes needed: "))
maxCases = ((2**K))**M

def generate_combinations(K, M, H):
    # Generate all possible K-bit numbers
    max_num = 2**K
    possible_numbers = range(max_num)
    
    # Generate all possible combinations of M K-bit numbers
    all_combinations = combinations_with_replacement(possible_numbers, M)
    
    # Filter combinations that sum to H
    valid_combinations = [comb for comb in all_combinations if sum(comb) == H]
    
    return valid_combinations


for i in range(H):
    combinations = generate_combinations(K, M, i)
    print(f"Total combinations: {len(combinations)}")
    for comb in combinations:
        print(comb)
