def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def generate_fibonacci_sequence(n):
    fibonacci_sequence = []
    for i in range(n):
        fibonacci_sequence.append(fibonacci_recursive(i))
    return fibonacci_sequence

# Example
num_terms = 10
fibonacci_numbers = generate_fibonacci_sequence(num_terms)
print("Fibonacci sequence:", fibonacci_numbers)
