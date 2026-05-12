from math_utils import annual_salary
from employee_utils import add_employee, show_employees,search_employee

while True:
    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. Show Employees")
    print("3. Search Employee")
    print("4. Calculate Annual Salary")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        department = input("Enter Department: ")
        salary = float(input("Enter Monthly Salary: "))

        add_employee(emp_id, name, age, department, salary)

    elif choice == "2":
        show_employees()

    elif choice == "3":
        emp_id = input("Enter Employee ID to search: ")
        search_employee(emp_id)

    elif choice == "4":
        salary = float(input("Enter Monthly Salary: "))
        print("Annual Salary:", annual_salary(salary))

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")