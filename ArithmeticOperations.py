def arithmetic_operation(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operator."
def arithmetic_operations():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    operator = input("Enter the operator (+, -, *, /): ")
    result = arithmetic_operation(a, b, operator)
    print(f"Result: {result}")

arithmetic_operations()
