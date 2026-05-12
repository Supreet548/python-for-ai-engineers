employees = {}
def add_employee(emp_id,name,age,department,salary):
    employees[emp_id]={
        "Name":name,
        "Age":age,
        "Department":department,
        "Salary":salary
    }

    print("Employess added successfully")


def show_employees():
    if not employees:
        print("No employees found")

        return
    
    print("\nEmployees List")
    print("-"*50)

    for emp_id, details in employees.items():
        print(f"ID: {emp_id}")
        for key, value in details.items():
            print(f"{key}: {value}")
        print("-" * 50)

def search_employee(emp_id):
    if emp_id in employees:
        print("\nEmployee Found")
        print("-"*50)

        for key, value in employees[emp_id].items():
            print(f"{key}: {value}")

    else:
        print("Employee not found.")



