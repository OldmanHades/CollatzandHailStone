import matplotlib.pyplot as plt


def hailstone_sequence(n):
    """
    This function generates the hailstone sequence for a given number n.

    Args:
        n: The starting integer.

    Returns:
        A list containing the hailstone sequence.
    """
    sequence = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    return sequence


def plot_hailstone(sequence):
    """
    This function plots the hailstone sequence data.
    """
    plt.plot(sequence)
    plt.xlabel("Step")
    plt.ylabel("Number")
    plt.title("Hailstone Sequence")
    plt.grid(True)
    plt.show()


def main():
    """
    This function interacts with the user, asks for input, and prints/plots the hailstone sequence.
    """
    while True:
        try:
            n = int(input("Enter a positive integer (-1 to quit): "))
            if n < 0:
                break
            elif n <= 0:
                print("Please enter a positive integer.")
                continue

            sequence = hailstone_sequence(n)
            print(f"Hailstone sequence for {n}: {sequence}")
            print(f"Length of sequence: {len(sequence)}\n")
            plot_hailstone(sequence)

        except ValueError:
            print("Invalid input. Please enter an integer.")


if __name__ == "__main__":
    main()
