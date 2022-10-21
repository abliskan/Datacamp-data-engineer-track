# Section1: OOP terminology
# True
"""
- Attributes
- Methods
- Encapsulation
"""
# False
"""
- Object and class are different terms describing the same concept 
- A programming language can be either object-oriented or procedural, but not both
- .column is an example of a method of a DataFrame object.
- Object is an abstract template describing the general states and behaviors
"""

# Section2: Exploring object interface
# Q1 = What class does the mystery object have?, A = __main__.Employee
# Q2 =
"""
# Print the mystery employee's name
print(mystery.name)

# Print the mystery employee's salary
print(mystery.salary)
"""
# Q3 =
"""
# Print the mystery employee's name
print(mystery.name)

# Print the mystery employee's salary
print(mystery.salary)

# Give the mystery employee a raise of $2500
mystery.give_raise(2500)

# Print the salary again
print(mystery.salary)
"""

# Section4: Understanding class definitions
"""
class MyCounter:
     def set_count(self, n):
           self.count = n
mc = MyCounter()
mc.set_count(5)
mc.count = mc.count + 1
print(mc.count)
"""

# Section5: Create your first class
# Q1 =
"""
# Create an empty class Employee
class Employee:
    def __init__(self):
        pass

# Create an object emp of class Employee 
emp = Employee()
"""
# Q2 =
"""
# Include a set_name method
class Employee:
  
  def set_name(self, new_name):
    self.name = new_name
  
# Create an object emp of class Employee  
emp = Employee()

# Use set_name() on emp to set the name of emp to 'Korel Rossi'
emp.set_name('Korel Rossi')

# Print the name of emp
print(emp.name)
"""
# Q3 =
"""
class Employee:
  
  def set_name(self, new_name):
    self.name = new_name
  
  # Add set_salary() method
  def set_salary(self, new_salary):
    self.salary = new_salary
  
# Create an object emp of class Employee  
emp = Employee()

# Use set_name to set the name of emp to 'Korel Rossi'
emp.set_name('Korel Rossi')

# Set the salary of emp to 50000
emp.set_salary(50000)
"""

# Section6: Using attributes in class definition
# Q1 =
"""
class Employee:
    def set_name(self, new_name):
        self.name = new_name

    def set_salary(self, new_salary):
        self.salary = new_salary 
  
emp = Employee()
emp.set_name('Korel Rossi')
emp.set_salary(50000)

# Print the salary attribute of emp
print(emp.salary)

# Increase salary of emp by 1500
emp.salary = emp.salary + 1500

# Print the salary attribute of emp again
print(emp.salary)
"""
# Q2 =
"""
class Employee:
    def set_name(self, new_name):
        self.name = new_name

    def set_salary(self, new_salary):
        self.salary = new_salary 

    # Add a give_raise() method with raise amount as a parameter
    def give_raise(self, is_give_raise):
        self.salary += is_give_raise


emp = Employee()
emp.set_name('Korel Rossi')
emp.set_salary(50000)

print(emp.salary)
emp.give_raise(1500)
print(emp.salary)
"""
# Q3 =
"""
class Employee:
    def set_name(self, new_name):
        self.name = new_name

    def set_salary(self, new_salary):
        self.salary = new_salary 

    def give_raise(self, amount):
        self.salary = self.salary + amount

    # Add monthly_salary method that returns 1/12th of salary attribute
    def monthly_salary(self):
        return self.salary / 12.0
    
emp = Employee()
emp.set_name('Korel Rossi')
emp.set_salary(50000)

# Get monthly salary of emp and assign to mon_sal
mon_sal = emp.monthly_salary()

# Print mon_sal
print(mon_sal)
"""

# Section7: Correct use of __init__
# A: 2

# Section8: Add a class constructor
# Q1 =
"""
class Employee:
    # Create __init__() method
    def __init__(self, name, salary=0):
        # Create the name and salary attributes
        self.name = name
        self.salary = salary
    
    # From the previous lesson
    def give_raise(self, amount):
        self.salary += amount

    def monthly_salary(self):
        return self.salary/12
        
emp = Employee("Korel Rossi")
print(emp.name)
print(emp.salary)     
"""
# Q2 =
"""
class Employee:
  
    def __init__(self, name, salary=0):
        self.name = name
        # Modify code below to check if salary is positive
        if salary >= 0:
            self.salary = salary 
        else:
            self.salary = 0
            print("Invalid salary!")
   
   # ...Other methods omitted for brevity ...
      
emp = Employee("Korel Rossi", -1000)
print(emp.name)
print(emp.salary)
"""
# Q3 =
"""
# Import datetime from datetime
from datetime import datetime 

class Employee:
    
    def __init__(self, name, salary=0):
        self.name = name
        if salary > 0:
          self.salary = salary
        else:
          self.salary = 0
          print("Invalid salary!")
          
        # Add the hire_date attribute and set it to today's date
        self.hire_date = datetime.today()
        
   # ...Other methods omitted for brevity ...
      
emp = Employee("Korel Rossi", -1000)
print(emp.name)
print(emp.salary)
"""

# Section9: Write a class from scratch
"""
# Write the class Point as outlined in the instructions
import math 

class Point: 
    
    # Constrctor to define the attributes 
    def __init__ (self,x=0,y=0):
        self.x = x 
        self.y = y
    
    def distance_to_origin(self): 
        return math.sqrt(self.x**2 + self.y**2)
    
    def reflect(self, axis): 
        
        if axis=="x":
            self.y = - self.y 
        elif axis =="y":
            self.x = - self.x
        else: 
            print("Invalid input, please input x or y")
        
pt = Point(x=3.0)
pt.reflect("y")
print((pt.x, pt.y))
pt.y = 4.0
print(pt.distance_to_origin())
"""