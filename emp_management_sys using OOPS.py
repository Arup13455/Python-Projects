# Employee Management System using OOPs in python
# Add a new employee to the system with details such as name, ID, position and salary.
class Employee:
    def __init__(self, name, emp_id, position, salary):
        self.name = name
        self.emp_id = emp_id
        self.position = position
        self.salary = salary
class Employee_Management_System:
    def __init__(self):
        self.employees = []
    def add_employees(self, employee):
        self.employees.append(employee)
    def display_employees(self):
        for employee in self.employees:
            print(f"Name: {employee.name}")
            print(f"ID: {employee.emp_id}")
            print(f"Position: {employee.position}")
            print(f"Salary: {employee.salary}")
    def update_employee(self, emp_id, new_position, new_salary):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                employee.position = new_position
                employee.salary = new_salary
                print("Employee's details updated successfully.")
    def remove_employee(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                self.employees.remove(employee)
                print("Employee's removed successfully.")
    def Search_employee(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                print(f"Name: {employee.name}")
                print(f"ID: {employee.emp_id}")
                print(f"Position: {employee.position}")
                print(f"Salary: {employee.salary}")
            else:
                print(f"Employee with ID, {emp_id} not found.")
emp_sys = Employee_Management_System()
emp1 = Employee("Arup", 101, "Manager", 50000)
emp2 = Employee("Ajay", 102, "Developer", 60000)
emp_sys.add_employees(emp1)
emp_sys.add_employees(emp2)
emp_sys.display_employees()
emp_sys.update_employee(101, "Senior Manager", 60000)
emp_sys.display_employees()
emp_sys.remove_employee(101)
emp_sys.display_employees()
emp_sys.Search_employee(101)
