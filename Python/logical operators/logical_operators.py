# AND : true when both operands are true

# Is_student = True
# Is_present = False

# print(Is_student and Is_present)

#or true when atleast one operand is true
# print(Is_student or Is_present)

#NOT : true when operand is false
# print(not Is_student)
# print(not Is_present)

#USE CASES:
#AND
#Returns true if both conditions are true otherwise false
# x = 10
# y = 20
# z = 30
# if x > y and y > z:
#     print("x is the largest number")
# else:
#     print("x is not the largest number")

#OR
#Returns true if one of the condition  is true otherwise false

# x = 30
# y = 50
# z = 10
# if x>y or x>z:
#     print("x is atleast larger than one number")
# else:
#     print("x is the smallest number")


#NOT
#Returns true if the conditional expression returns false and vice versa

# x = 10
# y = 20
# z = 30
# if not(x > y or x > z):
#     print("x is not the largest number")
# else:
#     print("x is not the smallest number")

#Other use cases:
#if you arec going outside and want to check the temperature

#  temp = int(input("what is the temperature outside: "))
# if temp >= 0 and temp <=30:
#     print("the temperature is good today")
#     print("go outside and enjoy")

# elif temp < 0 or temp > 30:
#     print("the temperature is bad today!")
#     print("stay inside and enjoy")

# if not(temp >= 0 and temp <=30):
#  print("the temperature is bad today!")
#  print("stay inside and enjoy")



# elif not(temp < 0 or temp > 30):
#  print("the temperature is good today")
#  print("go outside and enjoy") 


# temp = -15


# if temp > 0 and temp < 30:
#  print("the temperature is good today")
# else:
#     print("the temperature is bad today")


# if temp <= 0 or temp >= 30:
#     print("the temperature is bad today")
# else:
#      print("the temperature is good today")


temp = 20
sunny = True

if temp <= 0 or temp >= 30:
    print("the temperature is bad today")
else:
     print("the temperature is good today")
if not sunny:
     print("the sun is shining")
else:
     print("it is cloudy")
