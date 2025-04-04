class Students:
    
    def enroll(self):
        pass
    def graduate(self):
        pass
    
class Graduates(Students):
        def enroll(self):
            return "Enrolling in a graduate program"
            
        def graduate(self):
            return "graduating from enrolled program"
vague_student = Graduates()
print(vague_student.graduate())