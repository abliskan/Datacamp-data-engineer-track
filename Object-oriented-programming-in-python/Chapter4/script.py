# Section1: Polymorphic methods
"""
A: 4
"""
# Section2: Square and rectangle
"""
# Define a Rectangle class
class Rectangle:
    def __init__(self, h, w):
        self.h = h
        self.w = w

# Define a Square class
class Square(Rectangle):
    def __init__(self, w):
        Rectangle.__init__(self, w, w)
###############################################
A: The 4x4 Square object would no longer be a square if we assign 7 to h.
###############################################
class Rectangle:
    def __init__(self, w,h):
      self.w, self.h = w,h

# Define set_h to set h      
    def set_h(self, h):
      self.h = h
      
# Define set_w to set w          
    def set_w(self, w):
      self.w = w
      
      
class Square(Rectangle):
    def __init__(self, w):
      self.w, self.h = w, w 

# Define set_h to set w and h
    def set_h(self, h):
      self.h = h
      self.w = h

# Define set_w to set w and h      
    def set_w(self, w):
      self.h = w
      self.w = w
###############################################

A: Each of the setter methods of Square change both h and w attributes, while setter methods of Rectangle change only one attribute at a time, so the Square objects cannot be substituted for Rectangle into programs that rely on one attribute staying constant.
"""
# Section3: Attribute naming conventions
"""
# _name
A: A helper method that checks validity of an attribute's value but isn't considered a part of class's public interface
# __name
A: A 'verson' attribute that stores the current verion of the class and shouldn't be passed to child classes, who will have their own versions
# __name__
A: A method that is run whenever the object is printed
"""
# Section4: Using internal attributes
"""
# Add class attributes for max number of days and months
class BetterDate:
    _MAX_DAYS = 30
    _MAX_MONTHS = 12
    
    def __init__(self, year, month, day):
        self.year, self.month, self.day = year, month, day
        
    @classmethod
    def from_str(cls, datestr):
        year, month, day = map(int, datestr.split("-"))
        return cls(year, month, day)
    
    # Add _is_valid() checking day and month values
    def _is_valid(self):
        return (self.day <= BetterDate._MAX_DAYS) and (self.month <= BetterDate._MAX_MONTHS)
    
bd1 = BetterDate(2020, 4, 30)
print(bd1._is_valid())

bd2 = BetterDate(2020, 6, 45)
print(bd2._is_valid())
"""
# Section5: What do properties do?
"""
A: Properties can prevent creation of new attributes via assignment
"""
# Section6: Create and set properties
"""
# Create a Customer class
class Customer:

    def __init__(self, name, new_bal):
        self.name = name
        if new_bal < 0:
            raise ValueError
        else:
            self._balance = new_bal
###################################################
class Customer:
    def __init__(self, name, new_bal):
        self.name = name
        if new_bal < 0:
           raise ValueError("Invalid balance!")
        self._balance = new_bal  
    
    # Add a decorated balance() method returning _balance
    @property
    def balance(self):
        return self._balance
        class Customer:
    def __init__(self, name, new_bal):
        self.name = name
        if new_bal < 0:
           raise ValueError("Invalid balance!")
        self._balance = new_bal  
    
    # Add a decorated balance() method returning _balance
    @property
    def balance(self):
        return self._balance
###################################################
class Customer:
    def __init__(self, name, new_bal):
        self.name = name
        if new_bal < 0:
           raise ValueError("Invalid balance!")
        self._balance = new_bal  

    # Add a decorated balance() method returning _balance        
    @property
    def balance(self):
        return self._balance
     
    # Add a setter balance() method
    @balance.setter
    def balance(self, new_balance):
        # Validate the parameter value
        if new_balance < 0:
            raise ValueError
        else:
            self._balance = new_balance
        
        # Print "Setter method is called"
        print("Setter method is called")
###################################################
class Customer:
    def __init__(self, name, new_bal):
        self.name = name
        if new_bal < 0:
           raise ValueError("Invalid balance!")
        self._balance = new_bal  

    # Add a decorated balance() method returning _balance        
    @property
    def balance(self):
        return self._balance

    # Add a setter balance() method
    @balance.setter
    def balance(self, new_bal):
        # Validate the parameter value
        if new_bal < 0:
           raise ValueError("Invalid balance!")
        self._balance = new_bal
        print("Setter method called")

# Create a Customer        
cust = Customer("Belinda Lutz", 2000)

# Assign 3000 to the balance property
cust.balance = 3000

# Print the balance property
print(cust.balance)
"""
# Section7: Read-only properties
"""
import pandas as pd
from datetime import datetime

# LoggedDF class definition from Chapter 2
class LoggedDF(pd.DataFrame):
    def __init__(self, *args, **kwargs):
        pd.DataFrame.__init__(self, *args, **kwargs)
        self.created_at = datetime.today()

    def to_csv(self, *args, **kwargs):
        temp = self.copy()
        temp["created_at"] = self.created_at
        pd.DataFrame.to_csv(temp, *args, **kwargs)   

# Instantiate a LoggedDF called ldf
ldf = LoggedDF({"col1": [1,2], "col2":[3,4]}) 

# Assign a new value to ldf's created_at attribute and print
ldf.created_at = '2035-07-13'
print(ldf.created_at)
###################################################
import pandas as pd
from datetime import datetime

# MODIFY the class to use _created_at instead of created_at
class LoggedDF(pd.DataFrame):
    def __init__(self, *args, **kwargs):
        pd.DataFrame.__init__(self, *args, **kwargs)
        self._created_at = datetime.today()
    
    def to_csv(self, *args, **kwargs):
        temp = self.copy()
        temp["created_at"] = self._created_at
        pd.DataFrame.to_csv(temp, *args, **kwargs)   
    
    # Add a read-only property: _created_at
    @property  
    def created_at(self):
        return self._created_at

# Instantiate a LoggedDF called ldf
ldf = LoggedDF({"col1": [1,2], "col2":[3,4]}) 
###################################################
A: An AttributeError is thrown since ldf.created_at is read-only.
"""
