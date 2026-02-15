# Class Methods = Allow operations related to the class itself
#                 Take (cls) as the first parameter, which represents the class itself

class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1 #Increase count by 1 for every student that is created
        Student.total_gpa += gpa
    
    #Instance Method
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    #Class Method 1
    @classmethod
    def get_count(cls):
        return f"Total no of students: {cls.count}"
    
    #Class Method 2
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa: {cls.total_gpa / cls.count:.2f}"
    
    
student1 = Student("Spongebob", 3.2)
student2 = Student("Patrick", 2.0)
student3 = Student("Sandy", 4.0)

print(Student.get_count())
print(Student.get_average_gpa())