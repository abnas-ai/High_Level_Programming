#LIST COMPREHENSIONS
#LONG METHOD
# a = [1, 2, 3, 4, 5]
# change = []
# for y in a:
#     change.append(y*2)
# print(change)

#SHORT SYNTAX
# a = [1, 2, 3, 4, 5]
# change = [x*5 for x in a]
# print(change)


# nums = [0,1,2,3,4,5,6,7,8]
# nums2 = []
# for x in nums:
#      if x % 2==0:
#       nums2.append(x)
# print(nums2)

# nums = [0,1,2,3,4,5,6,7,8]
# nums2 = [x for x in range(9) if x % 2==0]
# print(nums2)


# numbers = [1,2,3,4,5]
# square_numbers = []
# for num in numbers:
#      square_numbers.append(num*num)
# print(square_numbers)

# numbers = [1,2,3,4,5]
# square_numbers = [num ** 2 for num in numbers]
# print(square_numbers)

# numbers = [1,2,3,4,5,6,7,8,9,10]
# square_of_even_numbers = []
# for number in numbers:
#     if number % 2 ==0:
#         square_of_even_numbers.append(number ** 2)
# print(square_of_even_numbers)


numbers = [1,2,3,4,5,6,7,8,9,10]
square_of_even_numbers = [numbers**2 for numbers in numbers if numbers % 2==0]
print(square_of_even_numbers)
