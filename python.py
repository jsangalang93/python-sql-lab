import psycopg2
import psycopg2.extras
connection = psycopg2.connect(database='companies')

cursor = connection.cursor()
    
#----------------------------------------GET------------------------------------------------------------------------------

#(EMPLOYEES)
cursor.execute("SELECT * FROM employees")
print(cursor.fetchall())

#(COMPANIES)
cursor.execute("SELECT * FROM companies")
print(cursor.fetchall())

#----------------------------------------CREATE------------------------------------------------------------------------------

#(EMPLOYEES)

def create_employees():
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


cursor.close()
connection.close() 