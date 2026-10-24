class regular_student:
    def __init__( self, name, final_marks):
        self.name = name
        self.final_marks = final_marks
        print(f"{self.name} has got {self.final_marks}")


class sports_student():
    def __init__( self, name, final_marks):
        self.name = name
        self.final_marks = final_marks
        if final_marks>95:
            print(f"{self.name} has got {self.final_marks}")
        else:
            self.final_marks += 5
            print(f"{self.name} has got {self.final_marks}") 

name=input("Enter the name of the student: ")
final_marks=int(input("Enter the final marks of the student: "))
option=int(input("Enter 1 for Regular Student, 2 for Sports student: "))
if option==1:
    regular_student(name, final_marks)
else:
    sports_student(name, final_marks)