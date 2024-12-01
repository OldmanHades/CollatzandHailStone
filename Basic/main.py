import random


def collatz(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence


# Example usage
n = 13
sequence = collatz(n)
print("Starting number:", n)
print("Sequence:", sequence)


def analyze_collatz(num_samples, max_value):
    max_length = 0
    avg_steps = 0
    for _ in range(num_samples):
        n = random.randint(1, max_value)
        steps = 0
        while n != 1:
            if n % 2 == 0:
                n //= 2
            else:
                n = 3 * n + 1
            steps += 1
        max_length = max(max_length, steps)
        avg_steps += steps
    avg_steps /= num_samples
    return max_length, avg_steps


# Example usage
num_samples = 10000
max_value = 1000
max_length, avg_steps = analyze_collatz(num_samples, max_value)
print("Max sequence length:", max_length)
print("Average steps to reach 1:", avg_steps)
