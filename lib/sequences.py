#!/usr/bin/env python3

def print_fibonacci(length):
    # Initialize the first two Fibonacci numbers
    fib_sequence = []
    
    if length > 0:
        fib_sequence.append(0)
    if length > 1:
        fib_sequence.append(1)
    
    # Generate the Fibonacci sequence up to the specified length
    for i in range(2, length):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    
    # Print the Fibonacci sequence
    print(fib_sequence)
