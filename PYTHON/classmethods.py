# Class Methods = Allow operations related to the class itself
#                 Take (cls) as the first parameter, which represents the class itself

class Student:

    count = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1 #Increase count by 1 for every student that is created
    
    #Instance Method
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    #Class Method
    @classmethod
    def get_count(cls):
        return f"Total no of students: {cls.count}"

print(Student.get_count())
