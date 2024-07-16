def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    return result


def divide_numbers_operations():
    a = float(input("Enter the numerator: "))
    b = float(input("Enter the denominator: "))
    result = divide_numbers(a, b)
    print(f"Result: {result}")
divide_numbers_operations()
