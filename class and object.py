class Student:
    roll= " "
    gpa = " "

    def Set_value(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"ROLL :{self.roll}, GPA :{self.gpa}")

Rahim = Student()
Rahim.Set_value(101, 3.37)
Rahim.display()

Karim = Student()
Karim.Set_value(102, 4.0)
Karim.display()
