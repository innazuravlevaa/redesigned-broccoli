import matplotlib.pyplot as plt

def generate_fibonacci(n):
    """
    Generate the first 'n' Fibonacci numbers.
    """
    fibonacci_sequence = [0, 1]
    for _ in range(2, n):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return fibonacci_sequence

def plot_fibonacci(sequence):
    """
    Plot the Fibonacci sequence using matplotlib.
    """
    plt.plot(sequence, marker='x', color='red', linestyle='-', markersize=7)
    plt.title('Fibonacci Sequence')
    plt.xlabel('Index')
    plt.ylabel('Fibonacci Value')
    plt.grid(True)
    plt.show()

def print_fibonacci(sequence):
    """
    Print the Fibonacci sequence.
    """
    print("Fibonacci Sequence:")
    for index, value in enumerate(sequence):
        print(f"F({index}) = {value}")

def main():
    n = 20  # Number of Fibonacci numbers to generate
    fibonacci_sequence = generate_fibonacci(n)
    
    # Print and plot the Fibonacci sequence
    print_fibonacci(fibonacci_sequence)
    plot_fibonacci(fibonacci_sequence)

if __name__ == "__main__":
    main()