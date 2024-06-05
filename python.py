import psycopg2
import psycopg2.extras
connection = psycopg2.connect(database='companies')

cursor = connection.cursor()
    
#----------------------------------------GET------------------------------------------------------------------------------

#(EMPLOYEES)
def read_employee():
    cursor.execute("SELECT * FROM employees")
    print(cursor.fetchall())

#(COMPANIES
def read_company():
    cursor.execute("SELECT * FROM companies")
    print(cursor.fetchall())

#----------------------------------------CREATE------------------------------------------------------------------------------

#(EMPLOYEES)

def create_employee():
    name = input("Enter Employee Name: ")
    company_id = input ("Enter Company ID: ")
    cursor.execute("INSERT INTO employees (name, company_id) VALUES (%s, %s)", (name, company_id))
    connection.commit()
print("Employee has been created successfully.")

#(COMPANIES)

def create_company():
    name = input("Enter Company Name: ")
    cursor.execute("INSERT INTO companies (name) VALUES (%s)", (name))
    connection.commit()
print("Company has been created successfully.")

#----------------------------------------UPDATE------------------------------------------------------------------------------

# (EMPLOYEES)
def update_employee():
    employee_id = input("Enter Employee ID: ")
    new_name = input("Enter Updated Employee Name: ")
    new_company_id = input ("Enter Updated Company ID: ")
    cursor.execute("UPDATE employees SET name = %s, company_id = %s WHERE id = %s", (new_name, new_company_id))
    connection.commit()
print("Employee Updated Successfully.")

#(COMPANIES)
def update_company():
    name = input ("Enter Company Name")
    new_name = input("Enter New Company Name: ")
    cursor.execute("INSERT INTO companies (name) VALUES (%s)", (name))
    cursor.execute("UPDATE companies SET name = %s WHERE id = %s", (new_name))
    connection.commit()
print("Company Updated Successfully.")

#----------------------------------------DELETE------------------------------------------------------------------------------

#(EMPLOYEES)
def delete_employee():
    employee_id = input ("Enter Employee ID you wish to delete: ")
    cursor.execute('DELETE FROM employees WHERE id = %s', [])
    connection.commit()
print("Employee Deleted Successfully.")

#(COMPANIES)
def delete_company():
    company_id = input ("Enter Company ID you wish to delete: ")
    cursor.execute('DELETE FROM companies WHERE id = %s', [])
    connection.commit()
print("Company Deleted Successfully.")


#----------------------------------------MENU------------------------------------------------------------------------------

while True:
    print('CRM MENU')
    
    print('1. Create Employee')
    print('2. Create Company')
    print('3. Read Employee')
    print('4. Read Company')
    print('5. Update Employee')
    print('6. Update Company')
    print('7. Delete Employee')
    print('8. Delete Company')
    print('9. Exit')
    
    choice = input("Enter your choice (1-9): ")
    if choice == '1':
        create_employee()
    elif choice == '2':
        create_company()
    elif choice == '3':
        read_employee()
    elif choice == '4':
        read_company()
    elif choice == '5':
        update_employee()
    elif choice == '6':
        update_company()
    elif choice == '7':
        delete_employee()
    elif choice == '8':
        delete_company()
    elif choice == '9':
        break
    else:
        print("Invalid Choice. Please select a valid option.")


        

cursor.close()
connection.close() 