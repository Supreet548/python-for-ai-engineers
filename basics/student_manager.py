class Student:

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")

students = []

for i in range(3):

    name = input("Enter name: ")
    marks = int(input("Enter marks: "))

    student = Student(name, marks)

    students.append(student)

for s in students:
    s.display()