students = ['Kirui', 'Rop', 'Dorothy']

#1 accessing items in a list
# print(students[1])
#2 Modifying elements in a list
students.append('Kipngeno')
# print(students)
#3 insert() method
students.insert(0, 'Enock')
#4 print(students)
teachers = ['Mr. Ben', 'Mr. Bett']
students.extend(teachers)
# print(students)
#5 Concatenation
africode_community = students + teachers
# print(africode_community)

#6 removing elements from list
students.remove('Mr. Ben')
# print(students)

students.pop(0)
# print(students)

del students[1]
# print(students)

# clear() method
students.clear()
print(students)