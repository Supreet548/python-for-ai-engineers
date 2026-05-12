students = []

while True:
    name = input("Enter student name: ")
    marks = input("Enter student marks: ")

    students.append({
        "name":name,
        "marks":marks
    })

    choice = input("Add another student?(Yes/No): ")

    if choice.lower()=="no":
        break

print("\nStudent Records: ")

for student in students:
    print(student)