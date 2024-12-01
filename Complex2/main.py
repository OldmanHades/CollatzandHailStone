import matplotlib.pyplot as plt
from numba import njit


@njit
def collatz_steps(n):
    """
    Calculates the number of steps in the Collatz sequence starting from n.

    Args:
        n: The positive integer to start with.

    Returns:
        The number of steps it takes for the Collatz sequence to reach 1.
    """
    steps = 0
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps


@njit
def generate_collatz_data(max_start):
    """
    Generates the number of Collatz steps for numbers from 1 to max_start.

    Args:
        max_start: The maximum starting number.

    Returns:
        Two lists:
            * starting_numbers: The list of starting numbers.
            * num_steps: The corresponding number of steps for each starting number.
    """
    starting_numbers = []
    num_steps = []
    for i in range(1, max_start + 1):
        starting_numbers.append(i)
        num_steps.append(collatz_steps(i))
    return starting_numbers, num_steps


# Example usage
max_start_value = 10000
starting_numbers, num_steps = generate_collatz_data(max_start_value)

# Plotting the Collatz sequence data
plt.plot(starting_numbers, num_steps)
plt.xlabel("Starting Number")
plt.ylabel("Number of Steps")
plt.title("Collatz Conjecture Visualization")
plt.show()
