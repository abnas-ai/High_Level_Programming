#list comprehension(long method)
students = ["enock", "kirui", "kipngeno"]
# students_present = []

# for x in students:
#     if "i" in x:
#         students_present.append(x)
# print(students_present)

#short method

students_present = [x for x in students if "i" in x]
print(students_present)
