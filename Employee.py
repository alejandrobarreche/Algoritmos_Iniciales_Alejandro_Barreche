

class Employee():
    """Python class to implement a basic version of a hotel employee.

    This Python class implements the basic functionalities of a hotel employee in a 
    simple hotel management system.

    Syntax
    ------
    obj = Employee(emp_id, name, position, salary)

    Parameters
    ----------
    [in] emp_id : int
        Unique identifier for the employee.
    [in] name : str
        Name of the employee.
    [in] position : str
        The job position of the employee (e.g., 'Receptionist', 'Housekeeper', 'Manager').
    [in] salary : float
        The salary of the employee.

    Returns
    -------
    obj : Employee
        Python object output parameter that represents an instance of the class Employee.

    Attributes
    ----------
    """
    #Here you start your code.

    id_empleados = []
    
    def __init__(self, emp_id, name, position, salary):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary
        
        
    #Getters y setters
    
    # Getter for emp_id
    def get_emp_id(self):
        if isinstance(self.emp_id, int):
            if self.emp_id not in Employee.id_empleados:
                Employee.id_empleados.append(self.emp_id)
                return self.emp_id
            else:
                raise ValueError("Este id ya está en uso por otro empleado")

    # Setter for emp_id
    def set_emp_id(self, value):
        if isinstance(value, int) and value > 0:
            if value not in Employee.id_empleados:
                # Elimina el antiguo ID y añade el nuevo
                Employee.id_empleados.remove(self.emp_id)
                Employee.id_empleados.append(value)
                # Establece el nuevo ID para el empleado
                self.emp_id = value
            else:
                raise ValueError("Employee ID already in use.")
        else:
            raise ValueError("Employee ID must be a positive integer.")

    # Getter for name

    def get_name(self):
        if isinstance(self.name, str):
            return self.name


    # Getter for position

    def get_position(self):
        if isinstance(self.position, str):    
            return self.position

    # Setter for position
    def set_position(self, value):
        if isinstance(value, str) and len(value) > 0:
            self.position = value
        else:
            raise ValueError("Position must be a non-empty string.")

    # Getter for salary

    def get_salary(self):
        if isinstance(self.salary, (int, float)) and self.salary > 0:
            return self.salary

    # Setter for salary

    def set_salary(self, value):
        if isinstance(value, (int, float)) and value > 0:
            self.salary = value
        else:
            raise ValueError("Salary must be a non-negative number.")
    




def main():
    #TESTING
    print("=================================================================")
    print("Test Case 1: Create an Employee.")
    print("=================================================================")
    employee1 = Employee(1, "John Doe", "Receptionist", 30000)

    if employee1.get_emp_id() == 1:
        print("Test PASS. The parameter emp_id has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if employee1.get_name() == "John Doe":
        print("Test PASS. The parameter name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if employee1.get_position() == "Receptionist":
        print("Test PASS. The parameter position has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if employee1.get_salary() == 30000:
        print("Test PASS. The parameter salary has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    # Position and Salary Update Test
    print("=================================================================")
    print("Test Case 2: Update Employee's Position and Salary.")
    print("=================================================================")
    employee1.set_position("Manager")
    employee1.set_salary(50000)

    if employee1.get_position() == "Manager":
        print("Test PASS. The employee's position has been correctly updated.")
    else:
        print("Test FAIL. Check the method set_position().")

    if employee1.get_salary() == 50000:
        print("Test PASS. The employee's salary has been correctly updated.")
    else:
        print("Test FAIL. Check the method set_salary().")

if __name__ == "__main__":
    main()
