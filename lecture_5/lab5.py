# Q1: Library Management System — Class + Methods
# Goal: Practice constructor, attributes, methods, and object creation.
# Create a class `LibraryBook` with:
# - Attributes: title, author, is_borrowed (default False)
# - Method: borrow() → marks book as borrowed
# - Method: return_book() → marks it as not borrowed

# Create 2 book objects and simulate borrowing/returning

# =========================================================
class LibraryBook:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"'{self.title}' has been borrowed.")
        else:
            print(f"'{self.title}' is already borrowed!")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"'{self.title}' has been returned.")
        else:
            print(f"'{self.title}' was not borrowed!")


book1 = LibraryBook("1984", "George Orwell")
book2 = LibraryBook("Python Programming", "John Doe")

book1.borrow()
book2.borrow()

book1.return_book()
book2.return_book()

book2.borrow()
# =========================================================

#  Q2: Email Validator System — Static Method
# Goal: Use static method as utility.
# Create a class `EmailTool` with:
# - @staticmethod: is_valid(email) → returns True if email contains '@' and ends with '.com'
# Test with a list of 5 emails, print only the valid ones

# =========================================================

class EmailTool:
    @staticmethod
    def isvalid(email):
        return '@' in email and email.endswith('.com')

emails = [
    "test@example.cm",
    "hi@gmail.com",
    "invalid",
    "user@yahoo.org",
    "admin@site.com"
]

for i in emails:
    if EmailTool.isvalid(i):
        print(i)
# =========================================================
#  Q 3: Employee Management — Inheritance + Method Override
# Goal: Inheritance and method overriding in a new business domain.
# Class: Employee(name, salary)
# Method: get_role() → returns "General Employee"

# Class: Manager(Employee)
# Override get_role() → returns "Manager"

# Class: Developer(Employee)
# Override get_role() → returns "Developer"

# Create one object of each and call get_role()

# =========================================================

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        
    def get_role(self):
        return 'General Employee'
    
class Manager(Employee):
    def get_role(self):
        return "Manager"

class Developer(Employee):
    def get_role(self):
        return "Developer"

emp = Employee("Ahmed", 5000)
mgr = Manager("Sara", 9000)
dev = Developer("Omar", 7000)

print(emp.get_role())
print(mgr.get_role())
print(dev.get_role())

# =========================================================

#  Q 4: Expense Tracker — Encapsulation with Private Fields
# Goal: Apply encapsulation (not repeating BankAccount).
# Class: ExpenseTracker
# - Private attributes: __total, __owner
# - Method: add_expense(amount)
# - Method: get_total()

# Create an object and simulate 3 expense additions, print total
# =========================================================

class ExpenseTracker:
    
    def __init__(self,total,owner):
        self.__total = total
        self.__owner = owner
        
    def get_total(self):
        return self.__total
     
    
    def add_expense(self,amount):
        if amount > 0 :
            self.__total += amount
        else:
            print('amount must be positive !')

    def get_owner(self):
        return self.__owner
    
tracker = ExpenseTracker(1400, "Mena")

tracker.add_expense(300)
tracker.add_expense(100)
tracker.add_expense(200)
print(tracker.get_total()) 
tracker.add_expense(-50)
print(tracker.get_owner())
# =========================================================

# Q 5: Rectangle Calculator — Abstract Base Class
# Goal: Use abc module in a new geometry context.
# Abstract class: Polygon with area() and perimeter()
# Implement classes:
# - Rectangle(width, height)
# - Triangle(base, height, side_a, side_b) (assume right triangle)

# Calculate area/perimeter of both

# =========================================================
from abc import ABC,abstractmethod

class Polygon:
    
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Polygon):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2
    
class Triangle(Polygon):
    def __init__(self, base, height, side_a, side_b):
        self.base = base
        self.height = height
        self.side_a = side_a
        self.side_b = side_b

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.base + self.side_a + self.side_b


rect = Rectangle(5, 3)
print("Rectangle Area:", rect.area())
print("Rectangle Perimeter:", rect.perimeter())

tri = Triangle(6, 4, 5, 7)
print("Triangle Area:", tri.area())
print("Triangle Perimeter:", tri.perimeter())

# =========================================================

#  Q 6: Course Enroll System — Operator Overload
# Goal: Use __add__, __str__ in education setting.
# Class Course(title, hours)
# - __add__ → adds hours of 2 courses into new Course("Combined", total_hours)
# - __str__ → returns "Course: title (X hours)"


# =========================================================
class Course:
    def __init__(self,title,hours):
        self.title = title
        self.hours = hours
        
    def __add__(self,other):
        if not isinstance(other,Course):
            return NotImplemented
        return Course('Combined',self.hours + other.hours)
    def __str__(self):
        return f"Course: {self.title} , {self.hours} hours"


course1 = Course("Python Basics", 20)
course2 = Course("Data Analysis", 30)

combined_course = course1 + course2

print(course1)
print(course2)
print(combined_course)
# =========================================================

#  Q 7: Inventory Manager — File Append with Logging
# Goal: Use file append mode with formatted writing.
# Write a function log_product(name, quantity)
# - Append this line to inventory.txt:
#   "Added: {name} - Quantity: {quantity}"

# Add 3 products, then read and display the file content


# =========================================================

def log_product(name,quantity):
    with open("inventory.txt","a") as file:
        file.write(f"Addedd : {name} - Quantity: {quantity}\n")

log_product("Laptop", 5)
log_product("Mouse", 20)
log_product("Keyboard", 10)



# =========================================================

# Q 8: Smart Grade Reader — JSON File
# Goal: Use json.load() to process structured data.
# File: students.json
# Content: list of student objects {name, grade}

# Read the file and print all students who scored > 85


# =========================================================

import json
with open("students.json","r") as file:
    students = json.load(file)
    
print("students with grade > 85:")
for students in students:
    if students["grade"] > 85:
        print(f'Student Name :-> {students['name']} - Student Grade :-> {students['grade']}')

# =========================================================
#  Q 9: Negative Discount Validator — Custom Exception
# Goal: Create your own exception without using any example from the file.
# Class: NegativeDiscountError(Exception) → "Discount must be non-negative"

# Function: apply_discount(price, discount)
# - Raise error if discount < 0
# - Else return price after discount

# Handle the exception in try/except


# =========================================================
class NegativeDiscountError(Exception):
    def __init__(self):
        super().__init__("Discount must be non-negative")

def apply_discount(price, discount):
    if discount < 0:
        raise NegativeDiscountError()
    return price - discount
try:
    final_price = apply_discount(1000, 50)
    print("Final price:", final_price)

except NegativeDiscountError as e:
    print("Error:", e)

# =========================================================
#  Q 10: API Reader — Movie Titles (NOT posts)
# Goal: Use real-world public API (not repeated post/title example).
# API: https://api.tvmaze.com/search/shows?q=star
# Task:
# - Fetch JSON response
# - Print the name of each show in the results
# ✅ Bonus: Count how many shows were returned.



# =========================================================
import requests

url = "https://api.tvmaze.com/search/shows?q=star"
response = requests.get(url)


data = response.json()
count = 0
for item in data:
    print(item["show"]["name"])
    count+=1

print("total shows: ",count)

# =========================================================
#  Q 11: Task Manager — Object List + JSON Save
# Goal: Combine OOP + list + JSON write
# Class: Task(title, completed)

# Create a list of Task objects (minimum 3)
# Convert them to dictionaries using __dict__
# Save to tasks.json using json.dump()

# =========================================================
class  Task:
    def __init__(self,title,completed):
        self.title = title
        self.completed = completed

tasks = [
    Task("Finish Python project", False),
    Task("Read a book", True),
    Task("Go for a walk", False)
]

tasks_dict = [task.__dict__ for task in tasks]

import json

with open("tasks.json", "w") as file:
    json.dump(tasks_dict, file, indent=4)

# =========================================================

#  Q 12: Secure Notes App — File Creation with Error Handling
# Goal: Use file creation + exception handling.
# Ask user for a note title.
# Try to create file using 'x' mode (exclusive)
# If file already exists, catch the FileExistsError and print a warning

# Write "New note created" inside the file

# =========================================================
note_title = input("Enter note title: ")

try:
    with open(f"{note_title}.txt", "x") as file:
        file.write(f"{note_title} created a New note\n")
    print(f"Note '{note_title}.txt' created successfully!")

except FileExistsError:
    print(f"Warning: Note '{note_title}.txt' already exists!")
except Exception as e:
    print("An error occurred:", e)
# =========================================================
#  Q 13: Company Hierarchy Tree — Polymorphism
# Goal: Use polymorphism with method override and looping.
# Base class: Staff → method: describe()
# Subclasses:
# - Intern → "Intern doing training"
# - TeamLead → "TeamLead managing projects"
# - HR → "HR recruiting employees"

# Create a list of Staff objects of different types and call .describe() in a loop

# =========================================================
class Staff:
    def describe(self):
        print("staff")
class Intern(Staff):
    def describe(self):
        print("Intern doing training")

class TeamLead(Staff):
    def describe(self):
        print("TeamLead managing projects")

class HR(Staff):
    def describe(self):
        print("HR recruiting employees")
staff_list = [
    Intern(),
    TeamLead(),
    HR(),
    Intern(),
    TeamLead()
]
for staff in staff_list:
    staff.describe()
# =========================================================
#  Q 14: Mini Calculator — Operator Overload with Validation
# Goal: Use __truediv__, __sub__, validation, exceptions.
# Class Number(value)
# - __add__, __sub__, __mul__, __truediv__

# If dividing by zero, raise ZeroDivisionError manually with a custom message

# =========================================================
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __sub__(self, other):
        return Number(self.value - other.value)

    def __mul__(self, other):
        return Number(self.value * other.value)

    def __truediv__(self, other):   
        if other.value == 0:
            raise ZeroDivisionError("can't divide by zero")
        return Number(self.value / other.value)

    def __str__(self):
        return str(self.value)

# Usage
a = Number(10)
b = Number(5)
c = Number(0)

print("Addition:", a + b)       
print("Subtraction:", a - b)    
print("Multiplication:", a * b) 

try:
    print("Division:", a / b)  
    print("Division:", a / c)   
except ZeroDivisionError as e:
    print("Error:", e)

# =========================================================
#  Q 15: CSV Contact Loader — Medium Integration Task
# Goal: Use csv.reader() and print formatted contacts.
# Create a file contacts.csv:
# name,email,phone
# Ali,ali@gmail.com,01000000000
# Sara,sara@yahoo.com,01111111111

# Read the file using csv.reader()
# Print each contact like:
#   "Ali - ali@gmail.com - 01000000000"

# =========================================================
import csv

try:
    with open("contacts.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        
        print("Contacts List:\n")
        for row in reader:
            print(f"{row[0]} - {row[1]} - {row[2]}")

except FileNotFoundError:
    print("contacts.csv file not found!")

except Exception as e:
    print("An error occurred:", e)

# =========================================================
