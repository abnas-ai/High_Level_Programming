
#methods - functions that belong to an object(defined in a class)

class student:
    def __init__(self, name, age, scores, id_number=None, courses=None):
        self.name = name
        self.age = age
        self.scores = scores
        self.id_number = id_number
        self.courses = [x for x in courses] if courses else []
        
    def pass_fail(self):
        if self.scores >= 50:
            return " an Average student"
        else:
            return "is a poor student"
    def is_active(self):
        if self.courses == []:
            return "Not enrolled"
        else:
            return "Enrolled"
        
dorothy = student("Dorothy", 20, 53, "AASE09", courses=["Python", "HTML"])
John = student("John", 30, 42, id_number="AASE010")
print(f"{dorothy.name} of ID {dorothy.id_number} is {dorothy.pass_fail()} and {dorothy.is_active()}")
print(f"{John.name} of ID {John.id_number} is {John.pass_fail()} and {John.is_active()}")