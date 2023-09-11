def print_fibonacci(length):
    pass
    fibonacci_sequence = []
    if length > 0:
       fibonacci_sequence.append(0)
    if length >= 2:
       fibonacci_sequence.append(1)
    for i in range(2, length):
       fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    print(fibonacci_sequence)