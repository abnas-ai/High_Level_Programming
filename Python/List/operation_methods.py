# 1 slicing in lists
# fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
# # print(fruits[1:4])
# # ommiting indices  
# print(fruits[:4])
# # negative indices
# print(fruits[:-2])
# step value: start:stop:step
# print(fruits[::3])

# 2 changing items
# fruits[2] = 'cherry'
# print(fruits)

#changing multiple items
# fruits[2:3] = ['orange', 'pineapple']
# print(fruits)

#3  sort method
# words = ['A', 'B', 'C', 'F', 'Y', 'a', 'b', 'c']
# fruits.sort()
# print(fruits)
#Ascending
# fruits.sort()
# print(fruits)

# #descending order
# fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
# fruits.sort(reverse=True)
# print(fruits)

#4 sorted()
# sorted_fruits = sorted('fruits')
# print(sorted_fruits)

#5  reverse()
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
# fruits.reverse()
# print(fruits)

#6 count
counts = fruits.count('apple')
# print(counts)

#7 index
print(fruits.index('cherry'))
