
student = {
    "name" : "Kirui",
    "age" : 20,
    "Is_student" : True,
    "Courses" : ["Math", "Science", "History"],
    "Graduation year" : 2025,
    "GPA" : 3.8
}
#Attribute - properties of an object
#method - functions that belong to an object

human = {
    "tribe" : "kalenjin",
    "age" : 80,
    "is_alive" : True,
    "hobbies" : ["fishing", "hiking", "reading"]
}
#a class is a blueprint for creating objects
class student:
    def __init__(self, name, age, id_number=None, courses=None):
        self.name = name
        self.age = age
        self.id_number = id_number
        self.courses = [x for x in courses] if courses else []
        
enock = student("Enock", 20, id_number="123456", courses=["python", "html"])
rop = student("Rop", 24, id_number="425374", courses=["Java", "Python"])
# print(f"student Name is {rop.name} and age is {rop.age} with courses")
print(f"Student Name is {rop.name} and age is {rop.age} studying {rop.courses} with id number {rop.id_number}")
