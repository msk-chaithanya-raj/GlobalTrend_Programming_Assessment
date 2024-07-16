import time

def execution_time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper

@execution_time_decorator
def computationally_expensive_task(n):
    total = 0
    for i in range(n):
        total += i ** 2
    return total
def execution_time_operations():
    n = int(input("Enter a number for the computationally expensive task: "))
    result = computationally_expensive_task(n)
    print(f"Result of the task: {result}")
execution_time_operations()
