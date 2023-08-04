import random

def is_attacking(q1, q2):
    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])

def has_attacking_queens(queens):
    for i in range(8):
        for j in range(i + 1, 8):
            if is_attacking(queens[i], queens[j]):
                return True
    return False

def generate_random_queens():
    queens = [(random.randint(1, 8), random.randint(1, 8)) for _ in range(8)]
    return queens

def find_successful_arrangements(num_arrangements=4):
    successful_arrangements = []
    
    while len(successful_arrangements) < num_arrangements:
        queens = generate_random_queens()
        if not has_attacking_queens(queens):
            successful_arrangements.append(queens)
    
    return successful_arrangements

if __name__ == "__main__":
    successful_arrangements = find_successful_arrangements()
    
    for idx, queens in enumerate(successful_arrangements, start=1):
        print(f"Successful Arrangement {idx}:")
        for q in queens:
            print(q)
        print()
