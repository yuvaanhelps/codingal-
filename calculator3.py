#take input of numbers from user and perform basic arithmetic operations
num1 = float(input("enter first number:"))
num2 = float(input("enter second number:"))
# check for value error and syntax error
try:
    operation = input("enter operation (+, -, *, /):")
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            raise ZeroDivisionError("division by zero is not allowed")
    else:
        raise ValueError("invalid operation")
    print("result:", result)
except (ValueError, ZeroDivisionError) as e:
    print("error:", e)