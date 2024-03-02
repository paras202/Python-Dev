import itertools

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def throw_three_dice():
    dice_outcomes = [1, 2, 3, 4, 5, 6]
    all_combinations = list(itertools.product(dice_outcomes, repeat=3))
    
    prime_occurrences = 0

    for combination in all_combinations:
        dice_sum = sum(combination)
        if is_prime(dice_sum):
            prime_occurrences += 1
            print(f"Roll: {combination}, Sum: {dice_sum} (Prime)")

    total_combinations = len(all_combinations)
    probability_prime = prime_occurrences / total_combinations

    print(f"\nTotal outcomes: {total_combinations}")
    print(f"Prime outcomes: {prime_occurrences}")
    print(f"Probability of getting a prime sum: {probability_prime:.4f}")

if __name__ == "__main__":
    throw_three_dice()
