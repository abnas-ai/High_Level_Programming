
# from math import kirui
# print{"Hello world"}

# a = 1
# b = 2

# def divide(a, b):
#     return a / b


# # results = divide(1, 0)
# # print(results)

# try:
    
#     results = divide(1, 0)
#     print(results)
# except ZeroDivisionError as e:
    
#     print(f"Error: {e}")
    
# except TypeError as e:
#     print(f"invalid input type! please enter a number")
    
# except:

#     print("an error occured")
    
# else:
#    print("excecution was successfull")
# finally:
#     print("Iam being executed no matter what")

#******SYNTAX/COMPILLE TIME ERRORS***happns when python deosn't understand written code
#***Indentation error*****
# def func(): # indentation error
# return None
#****syntax error***8
# def func): #invalid syntax
#      return None

#******Exception/Runtime errors******happens during execution of a pogram
# print("Hello" + 5)
# print(dorothy)
#  other exception errors
""""
Value error
ZeroDivisionError
KeyError
IndexError
FileNotFoundError
"""
#*****Logical error******

# def sum(a,b):
#   return a/b
# result = sum(10, 3)
# print(result)

#HANDLING MULTIPLE ERRORS

try:
    number = int(input("Enter a number: "))
    results = 10/number
except Exception as e:
    print(f"ERROR: {e}")
else:
    print(results)
finally:
    print("Thanks for using our calc program")