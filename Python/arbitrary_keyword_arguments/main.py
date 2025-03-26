# #arbitrary args/kwargs
# def course_units(*args):
#      units = []
#      for unit in args:
#          units.append(unit)
#      return units
# units = course_units("Html5", "CSS", "JS", "Python", "Database", "Flask", True, 90, ["laptop", "phone"], {"name": "Enock", "age" : 20})
# print(units)

# def student_info(**info):
#     for key, value in info.items():
#         # return key, value
#         print(f"{key}: {value}")
# student_info(name="Enock", age=20, course="Python", score=90 )

# def performance_report(*args, **kwargs):
#     print(args)
#     print(kwargs)
# performance_report({"name" :"Kirui", "age" : 19, "score" : 90, "grade" : "A"},"Html5", "CSS", "JS", "Python", "Database", "Flask" , 90)

# def student_info(**info):
#     print(info)
    
# student_info(name="Rop", age=21, course="computrer science" status="active")

# def courses(*args):
#     print(args)
# courses("Html5", "CSS", "JS", "Python", "Database", "Flask", True, 90, ["laptop", "phone"], {"name": "Enock", "age" : 20})



# def courses(*args):
        
# student_courses = []
# for course in args:
#     student_courses.append(course)
# print(student_courses)
# courses("Html5", "CSS", "JS", "Python", "Database", "Flask")



#lambda functions
x = lambda x, y: x + y

print(x(5, 8))

def xy(a, b):
    print(a + b)
a = xy
a(5, 8)