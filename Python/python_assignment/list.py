# thislist = [15, 16, 17, 15, 15, 18, 20, 16, 20, 20, 25, 23, 26, 30, 33]
# x = sum(thislist)
# # print(x)



# lowest = min(thislist)
# print(lowest)

# highest = max(thislist)
# print(highest)


# num1 = float(input("Enter first number: "))
# operator = input("Enter operator (+, -, *, /): ")
# num2 = float(input("Enter second number: "))

# if operator == '+':
#  result = num1 + num2
# elif operator == '-':
#  result = num1 - num2
# elif operator == '*':
#  result = num1 * num2
# elif operator == '/':
#  if num2 == 0:
#   print("Error: Division by zero is not allowed.")
# result = num1 / num2

# print(f"{num1} {operator} {num2} = {result}")






# num1 = float(input("Enter first number: "))
# operator = input("Enter operator (+, -, *, /): ")
# num2 = float(input("Enter second number: "))

# if operator == '+':
#     result = num1 + num2
# elif operator == '-':
#     result = num1 - num2
# elif operator == '*':
#     result = num1 * num2
# elif operator == '/':
#     if num2 == 0:
#             print("Error: Division by zero is not allowed.")
#             result = None
#     else:
#             result = num1 / num2
# else:
#     print("Invalid operator! Use +, -, *, or /.")
# result = None

# if result is not None:
#      print(f"Result: {result}")



#Task: Create a program that takes three inputs (first number, operator, second number)
 and outputs the result of the calculation. The program should handle invalid inputs and division by zero errors.

try:
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            result = None
        else:
            result = num1 / num2
    else:
        print("Invalid operator! Use +, -, *, or /.")
        result = None

    if result is not None:
        print(f"Result: {result}")

except ValueError:
    print("Invalid input! Please enter numeric values.")