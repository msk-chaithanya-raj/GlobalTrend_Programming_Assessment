def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_operations():
    n = int(input("Enter n to compute the nth Fibonacci number: "))
    print(f"Fibonacci number at position {n}: {fibonacci(n)}")

fibonacci_operations()
