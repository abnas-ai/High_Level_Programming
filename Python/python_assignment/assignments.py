#create  a list of numbers (2 to 3 similar numbers) and create a program that :
#adds all the numbers
#checks the number with the lowest value
#checks the number with trhe highest value


# thislist = [15, 16, 17, 15, 15, 18, 20, 16, 20, 20, 25, 23, 26, 30, 33]
# x = sum(thislist)
# # print(x)



# lowest = min(thislist)
# print(lowest)

# highest = max(thislist)
# print(highest)



# temperature = 30
# print("It's a hot day")
# if temperature < 10:
#  print("It's a cold day")
# else:
#  print("It's neither hot or cold")


# temperature = 35
# if temperature > 30:
#     print("It's a hot day")
# else:
#     print("It's not a hot day")



# name = "John smith" 

# if len(name) < 3:
#  print("Name must be at least 3 characters")
# elif len(name) > 50:
#  print("Name can be a maximum of 50 characters")
# else:
#  print("Name looks good")



# weight = int(input("weight: "))
# unit = input("(L)bs or (K)g: ")
# if unit.upper() == "L":
#      converted = weight * 0.45
#      print(f"You are {converted} kilos")
# else:
#      converted = weight / 0.45
#      print(f"You are {converted} pounds")


# first_name = "Bro"
# second_name = "code"
# full_name = first_name +" "+ second_name
# print("Hello " + full_name)

# height = 250.5
# print("Your height is: " + str(height))

# name = "Bro code"
# # print(len(name))
# print(name.find("e"))

# name = input("What is your name: ")
# age = int(input("How old are you: "))
# age = age + 1
# print("Hello "+name)
# print("You are "+str(age)+" years old")


# name = input("What is your name: ")
# age = int(input("What is your age: "))
# age = age + 1
# print("Hello " +name)
# print("You are "+str(age)+" years old")


# #Task: Create a program that takes three inputs (first number, operator, second number)
# #  and outputs the result of the calculation. The program should handle invalid inputs and division by zero errors.


# #****TRIAL 1*****

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



# #Task: Create a program that takes three inputs (first number, operator, second number)
# #  and outputs the result of the calculation.


# #****TRIAL 2*****


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



#*******FINAL TRIAL********

# try:
#     num1 = float(input("Enter first number: "))
#     operator = input("Enter operator (+, -, *, /): ") 
#     num2 = float(input("Enter second number: "))

#     if operator == '+':
#         result = num1 + num2
#     elif operator == '-':
#         result = num1 - num2
#     elif operator == '*':
#         result = num1 * num2
#     elif operator == '/':
#         if num2 == 0:
#             print("Error: Division by zero is not allowed.")
#             result = None
#         else:
#             result = num1 / num2
#     else:
#         print("Invalid operator! Use +, -, *, or /.")
#         result = None

#     if result is not None:
#         print(f"Result: {result}")

# except ValueError:
#     print("Invalid input! Please enter numeric values.")

#Loop control statements******
#They change a loop execution from its normal sequence
# examples:
#1)*Break-Used to terminate the loop entirely
#use case:

# while True:
#      name = input("Enter your name: ")
#      if name != "":
#          break

#2)*Continue-Skips to the next iteration of the loop
#use case:
# phone_number = "123-456-7890"
# for i in phone_number:
#        if i == "-":
#          continue
#        print(i, end=" ")

#3)*Pass-Acts as a placeholder
#use case:
# for i in range(1,21):
#  if i == 13:
#      pass
# else:
#      print(i)


#****2D LISTS*****
#2D Lists is a list of lists
#use case:
drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice scream"]

food = [drinks, dinner, dessert]
# print(food)

#access a list and an item
#use case:
#access a list
# print(food[0])
#access one item:
#use case:
# print(food[0][0])

#*****DICTIONARIES*****
#A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
#Accessing items:
#use case:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
# print(x)
#****OR***
x = thisdict.get("model")
# print(x)


#****THE get() Method*****
#The get() method returns the value of the item with the specified key.
#use case:
#****get specific value****
x = thisdict.get("model")
#***get list of all the keys****
# x = thisdict.keys()
# print(x)


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
car["color"] = "red"
print(x) 

