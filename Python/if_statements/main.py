
# is_present = True

# if is_present:
#     print("start the lesson")
# else:
#     print("skip the lesson")


# age = 18
# is_citizen = False
# has_passport = False

# if age >= 18  and is_citizen:
#     print("you are eligible to vote")
# elif is_citizen and has_passport:

#     print("you are eligible to vote but you are not a citizen")

# else:

#     print("you are not eligible to vote")

# monthly_income = int(input("enter your monthly income: ")) # 30,000
# rent = int(input("enter your monthly rent: ")) #10,000
# takeout_budget = int(input("enter your monthly takeout budget: ")) #4000
# actual_takeout = int(input("enter your actual takeout: ")) #8000
# savings_goal = int(input("Enter your savings goal: ")) #5000

# if rent > monthly_income * 0.3:
#     print("you are spending too much on rent")
# if takeout_budget < actual_takeout:
#     print(f"you have blown your takeout budget by Kshs. {actual_takeout - takeout_budget}")
# elif monthly_income - rent - actual_takeout < savings_goal:
#     print("your rent is eating your paycheck like an hungry hippo")
# else:
#     print("you are doing great")
#     print(f"you have {monthly_income - rent - actual_takeout} left to save")


   # *******Shopping cart Decision Tree******
#    cart_total = 78
# distance_to_free_shipping = 22
# items_in_cart = ["sensible shoes, "Questionable fast food", "Items you dont need"]


#*******create a program that adds,subtracts,multiply or add two numbers**************



# num1 = float(input("Enter a number: "))
# operator = input("Enter operator: (+, -, *, /): ")
# num2 = float(input("Enter second number: "))

# if operator == "+":
#    result = num1 + num2
# elif operator == "-":
#     result = num1 - num2
# elif operator == "*":
#      result = num1 * num2
# elif operator == "/":
#     if num2 == 0:
#      print("Error! division by zero not allowed.")
#      result = None
#     else:
#      result = num1 / num2
# else:
#      print("invalid operator! use +,-, *, or /")
#      result = None
# if result is not None:
#      print(f"Result: {result}")












num1 = float(input("Enter first number: "))
operator = input("Enter operator: (+, -, *, /): ")
num2 = float(input("Enter second number: "))
if operator == "+":
    result = num1 + num2
elif operator == "*":
     result = num1 * num2
elif operator == "-":
     result = num1 - num2
elif operator == "/":
     if num2 == 0:
      print("Error! division by zero not allowed.")
     result = None
else:
     result = num1 / num2

if result is not None:
    print(f"Result: {result}")

    
