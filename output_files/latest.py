# Function to generate Fibonacci sequence up to n
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Print the first 40 numbers in the Fibonacci sequence
print(fibonacci(40))
