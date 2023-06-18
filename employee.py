import csv
# Define global variables
employee_fields = ['EmpId', 'name', 'age', 'email', 'phone']
employee_database = r"D:\visual studio programs\employeee_database.csv"


def display_menu():
    print("--------------------------------------")
    print(" Welcome to Employee Management System")
    print("---------------------------------------")
    print("1. Add New Employee")
    print("2. View Employeees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Quit")


def add_employee():
    print("-------------------------")
    print("Add Employee Information")
    print("-------------------------")
    global employee_fields
    global employee_database


    employee_data = []
    for field in employee_fields:
        value = input("Enter " + field + ": ")
        employee_data.append(value)

    with open(employee_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([employee_data])

    print("Data saved successfully")
    input("Press any key to continue")
    return


def view_employees():
    global employee_fields
    global employee_database

    print("--- employee Records ---")

    with open(employee_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in employee_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")

        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")

    input("Press any key to continue")


def search_employee():
    global employee_fields
    global employee_database

    print("--- Search Employee ---")
    EmpId = input("Enter empId to search: ")
    with open(employee_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if EmpId == row[0]:
                    print("----- Employee Found -----")
                    print("Empid: ", row[0])
                    print("Name: ", row[1])
                    print("Age: ", row[2])
                    print("Email: ", row[3])
                    print("Phone: ", row[4])
                    break
        else:
            print("EmpId not found in our database")
    input("Press any key to continue")


def update_employee():
    global employee_fields
    global employee_database

    print("--- Update Employee ---")
    EmpId = input("Enter empId to update: ")
    index_employee = None
    updated_data = []
    with open(employee_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if EmpId == row[0]:
                    index_employee = counter
                    print("Employee Found: at index ",index_employee)
                    employee_data = []
                    for field in employee_fields:
                        value = input("Enter " + field + ": ")
                        employee_data.append(value)
                    updated_data.append(employee_data)
                else:
                    updated_data.append(row)
                counter += 1


    # Check if the record is found or not
    if index_employee is not None:
        with open(employee_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("EmpId not found in our database")

    input("Press any key to continue")


def delete_employee():
    global employee_fields
    global employee_database

    print("--- Delete employee ---")
    EmpId = input("Enter EmpId to delete: ")
    employee_found = False
    updated_data = []
    with open(employee_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if EmpId != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    employee_found = True

    if employee_found is True:
        with open(employee_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("EmpId ", EmpId, "deleted successfully")
    else:
        print("EmpId not found in our database")

    input("Press any key to continue")

while True:
    display_menu()

    choice = input("Enter your choice: ")
    if choice == '1':
        add_employee()
    elif choice == '2':
        view_employees()
    elif choice == '3':
        search_employee()
    elif choice == '4':
        update_employee()
    elif choice == '5':
        delete_employee()
    else:
        break

print("-------------------------------")
print(" Thank you for using our Employee website")
print("-------------------------------")
