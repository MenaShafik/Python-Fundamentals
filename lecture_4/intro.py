# ------------------------------------------
# 0. Introduction
# ------------------------------------------
# high-level, English-Like Syntax, Dynamic
# Compiled / Interpreted
# Compiled: Your .py code is first compiled into bytecode (.pyc files) by the Python interpreter
# Interpreted: That bytecode is then interpreted by the Python Virtual Machine (PVM)
# PyInstaller or Cython: Can compile Python into machine code or standalone executables

# Guido Van Rossum => 20/02/1991
# Monty Python's Flying Circus => Not the snake

# Usage:
# Web Development => Flask, Django, FastAPI
# Data Science => Pandas, NumPy, scikit-learn
# Automation => Scripts, bots
# Desktop Apps => PyQt, Tkinter
# AI, Machine Learning => TensorFlow, PyTorch
# IoT => Raspberry Pi with Python
# Cybersecurity => Pen-testing scripts

# Install Latest Version of Python 3.14.2
# Important: ✅ Add python.exe to PATH

# Check Installation Successful:
# python --version
# pip --version


# Terminal => python
# Python Interactive Shell (REPL)

# IDE => VS Code + Extension (Python + Code Runner + Black Formatter + Pylance)
# PyCharm


# file_name.py
# Terminal (Ctrl + `) or (Ctrl + J): python file_name.py
# Code Runner => Press Triangle Button (Run Code)

# ------------------------------------------
# 1. Commenting => ignored by interpreter
# ------------------------------------------
# 1. Using Consecutive # Symbols
# 2. Using Triple Quotes (''' ... ''' or """ ... """) but not assigned to variable
# 3. For Documentation Strings (Docstrings)

# => Single Line Comment

# print("Hello Data Engineering Track")

"""
print("Hello Data Engineering Track")
print("Hello Data Engineering Track")
print("Hello Data Engineering Track")
"""


"""
Multi - Line
Comment
Docstrings - Documentation
"""


# ---------------------------------------
# 2. Basic Output:
# ---------------------------------------
from random import random

print("Hello Data Engineering Track", "Python", sep="*", end="\n\n")

# Windows => \r\n (CRLF)
# Linux/Unix => \n

# ---------------------------------------
# 3. Variables Initialization:
# ---------------------------------------
# 0x0000154515c156a => Example Memory Address
age = 15
print(age)

age = 25  # Reassignment
print(age)


# age = "Hassan" # Incompatible types in assignment (expression has type "str", variable has type "int")
# print(age)

# ---------------------------------------
# 4. Naming Conventions/Rules:
# ---------------------------------------

# must start with _ or letter
# can't start with numbers
# can include numbers and underscores
# case-sensitive

_variable1 = "Python is Great"


# Common naming styles: camelCase, PascalCase, snake_case

# snake_case ✅
first_name = "Hassan"

# camelCase
firstName = "Veronia"

# PascalCase
FirstName = "Ahmed"

# kebab-case / dash-case / hyphen-case ❌
# (kebab-case is not valid for Python variables) => used in HTML, CSS, URLs
# item-one = 1


# ---------------------------------------
# 5. Data Types and Type Checking
# ---------------------------------------

# Python Core Data Types (Primitives):

# int => 5, 15 => Whole Numbers
x = 5
# float => 5.2  => Decimal Numbers
y = 15.9
# complex => 3 + 5j => Complex numbers (real + imaginary)
z = 3 + 5j

# str => "Hello" => Text surrounded by quotes
str1 = "Hello"

# bool => True/False => Logical Values
is_student = False

# None => No value / null object
no_value = None

# ---------------------------------------------------------

# type()
print(type(no_value))
print(type(is_student))
print(type(str1))
print(type(y))
print(type(x))
print(type(z))

# ---------------------------------------------------------

# Sequences => list, tuple, range
# Lists: Ordered, mutable collection
fruits = ["apple", "Banana", "Cherry"]
print(fruits)
print(type(fruits))

# Tuples: Ordered, immutable collection
colors = ("red", "blue")
print(type(colors))


# Range: Sequence of numbers
nums = range(5)
print(nums)
print(type(nums))

# Set: Unordered, no duplicate items
my_set = {1, 2, 3, 4, 4}
print(my_set)
print(type(my_set))
# frozenset: Immutable set
frozen = frozenset([1, 2, 3])
print(type(frozen))  # <class 'frozenset'>

# Mapping => dict: Key-value pairs
person = {"name": "Ayman", "age": 23}
print(type(person))  # <class 'dict'>

# Binary => bytes, bytearray, memoryview
# bytes: Immutable binary data
data = b"hello"
print(type(data))  # <class 'bytes'>

# bytearray: Mutable binary data
mutable_data = bytearray(b"hello")
print(type(mutable_data))  # <class 'bytearray'>

# memoryview: Views over binary data
mv = memoryview(b"abc")
print(type(mv))  # <class 'memoryview'>


# ---------------------------------------
# 6. Input
# ---------------------------------------
# name = input("Please, enter your name: ")
# print(name)
# print(type(name))


# age1 = int(input("Please, enter your age: "))
# print(age1)
# print(type(age1))


# ---------------------------------------
# 7. Type Casting (Conversion)
# ---------------------------------------
# int()
old = "12345"
print(type(old))
new = int(old)
print(type(new))

# float()
# str()


# bool()
print(bool(0))
print(bool(""))
print(bool("Hello"))
print(bool(99))

letter = "A"
print(type(letter))
sentence = "Hello Mahmoud"
print(type(sentence))


# ---------------------------------------
# 8. Special characters in strings:
# ---------------------------------------
# New Line => \n
sentence = "Hello Mahmoud\nMy age is 23"
print(sentence)

# Escaping Double Quotes => \"
sentence = 'Hello "Mahmoud"\nMy age is 23'
print(sentence)


# Escaping Single Quotes => \'
sentence = "Hello 'Mahmoud'\nMy age is 23"
print(sentence)


# Escaping backslash => \\
sentence = "Hello \\Mahmoud\\\nMy age is 23"
print(sentence)


# ---------------------------------------
# 9. Operators Type:
# ---------------------------------------
# 1. Unary Operators
x = 5
variable_name = +5
variable_name = -5


# 2. Binary Operators
variable_name + variable_name


# 3. Ternary Operators
age = 20
state = "Adult" if age >= 18 else "Minor"


# ---------------------------------------
# 10. Operations:
# ---------------------------------------
# 1. Arithmetic Operators + - * / % // **
# Addition +:
item_one = 5
item_two = 10
result = item_one + item_two
print("The result of Summation is", result)

# Subtraction -:
result = item_two - item_one
print("The result of Subtraction is", result)

# Multiplication *:
result = item_two * item_one
print("The result of Multiplication is", result)


# Normal Division / => Implicit Casting:
result = item_one / item_two
print(type(result))
print("The result of Normal Division is", result)


# Floor Division // => Neglect Decimals
result = item_one // item_two
print(type(result))
print("The result of Floor Division is", result)

result = -7 // 2  # => Nearest -
print(type(result))
print("The result of Floor Division is", result)


# Remainder (% Modulus)
item_one = 10
item_two = 3

result = item_one % item_two
# 10 / 3 = 3.33333 => 0.33333 * 3 = 1
print("The result of Floor Division is", result)

# Exponent (Power)
x = 2**3
print(x)

# ---------------------------------------------------------

# Comparison Operators Result (bool): < > == <= >= !=
x = 10 > 5
print(x)

x = 10 < 5
print(x)


x = 10 == 5
print(x)

x = 10 != 5
print(x)

# ---------------------------------------------------------

# Logical Operators: and, or, not
# AND Logical Operator => All False Except for True = True and True
logic = 10 < 5 and 9 < 20  # False and True = False
print(logic)

# OR Logical Operator => All True Except for False = False or False
logic = 10 < 5 or 9 < 20  # False or True = True
print(logic)

# NOT Logical Operator
logic = not 10 < 5  # not False = True
print(logic)


# ---------------------------------------
# 11. Truthy or Falsy:
# ---------------------------------------
print("=========== Truthy and Falsy ===========")
# Truthy: bool(value) => True
x = 10
print(bool(10))

x1 = "Hello"
print(bool(x1))

x2 = True
print(bool(x2))

# Falsy: bool(value) => False
# False, [], (), {}, range(0), set(), "" , 0, 0.0, 0j, None
x2 = False
print(bool(x2))

x3 = None
print(bool(x3))

x3 = 0
print(bool(x3))


x4 = 0.0
print(bool(x4))


x6 = 0j
print(bool(x6))


x5 = ""
print(bool(x5))


empty_list = []
print(bool(empty_list))


empty_tuple = ()
print(bool(empty_tuple))


empty_dict = {}
print(bool(empty_dict))


empty_set = set()
print(bool(empty_set))


empty_range = range(0)
print(bool(empty_range))
print("----------------------------------------")

# ---------------------------------------
# 12. Control of Flow:
# ---------------------------------------
# Sequence

# Selection/Conditional Statements
# IF Statement (: + Indentation)
"""
if condition:
    # Block of Code
"""

# temp = int(input("Please enter the temperature: "))
# if temp > 30:
#     print("Weather is hot!")

# print("Normal Flow")

# IF-ELSE Statement
"""
if condition:
    # if Block
else:
    # else Block
"""

# temp = int(input("Please enter the temperature: "))
# if temp > 30:
#     print("Weather is hot!")
# else:
#     print("Weather is cold!")

# print("Normal Flow")

# IF-ELIF-ELSE Statement
"""
if condition1:
    # if Block

elif condition2:
    # elif Block

else:
    # else Block
"""

# Hint: Conditions must be in descending order


# temp = int(input("Please enter the temperature: "))
# if temp >= 30:
#     print("Weather is hot!")

# elif temp >= 20:
#     print("Weather is Moderate!")

# else:
#     print("Weather is cold!")

print("Normal Flow")

# ---------------------------------------------------------

# Python 3.10 (match ... case) => Replace switch in other languages
# No break is needed (unlike C/C++/Java)
"""
match expression:
    case pattern_1:
        # executed if pattern_1 matches
    case pattern_2:
        # executed if pattern_2 matches
    case _:
        # default case (like "default" in switch)
"""

status_code = 404

match status_code:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown Status")


# day = int(input("Please enter the day of the week order: "))
day = 5
# Sunday 1 => Saturday => 7

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")
    case 6 | 7:
        print("Weekend")
    case _:
        print("Invalid Input")

print("Normal Flow")

# Looping/Iterating
# print("Normal Flow")
# print("Normal Flow")
# print("Normal Flow")
# print("Normal Flow")
# print("Normal Flow")
# print("Normal Flow")
# print("Normal Flow")
# print("Normal Flow")


# range() => sequence of numbers => to show real value you must convert to list
# range(start, excluded end, step)
print(
    list(range(5))
)  # 1 arg => stop (Excluded) => start from 0 and stop at 5 (Excluded)

print(
    list(range(1, 5))
)  # 1 arg => stop (Excluded) => start from 1 and stop at 5 (Excluded)


print(
    list(range(1, 5, 2))
)  # 1 arg => stop (Excluded) => start from 1 and stop at 5 (Excluded) and step 2

# ---------------------------------------------------------

# Definite Iteration (for)
for i in range(1, 5, 2):
    print(i)

print("Normal Flow")


for char in "abc":
    print(char)

print("Normal Flow")


for n in [1, 2, 3]:
    print(n)

print("Normal Flow")

# ---------------------------------------------------------

# Indefinite Iteration (while) => infinite loop
"""
while condition:
    #Block if Code
"""

# Password => No Security/No limitation
# actual_password = "python123"
# entered_password = ""

# while entered_password != actual_password:
#     entered_password = input("Please enter your password: ")
# print("Access Granted")

# ---------------------------------------------------------

# iterator - condition - step
i = 0
while i < 5:  # 5 Excluded
    print(i)
    # i = i + 1
    i += 1  # Compound Assignment Operator


i = 0
while i <= 5:  # 5 Included
    print(i)
    # i = i + 1
    i += 1  # Compound Assignment Operator

# ---------------------------------------------------------

# break => Exit Loop completely

# while True:
#     command = input(">> ")
#     if command == "exit":
#         break

for i in range(5):
    print(i)
    if i == 3:
        break


# ---------------------------------------------------------

# continue => skip current iteration and continue
for i in range(5):
    if i == 3:
        continue
    print(i)


# ---------------------------------------------------------

# pass => Does Nothing (Placeholder) Planning for structure
print("Before Pass")

for i in range(5):
    pass

print("After Pass")

# ---------------------------------------------------------

# else with loops => to check whether loop breaks or not
for i in range(5):
    print(i)
else:
    print("Else executed")
    print("Loop completed successful without breaks")


print("----------- Break -----------")


for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("will not executed due to break")


print("----------- Continue -----------")


for i in range(5):
    if i == 3:
        continue
    print(i)
else:
    print("will executed")


# ---------------------------------------
# 13. Functions:
# ---------------------------------------
# def function_name(parameters_list):
#     # Function Body
#     pass


# function_name()


# 1. No Positional Parameters, No Return
def greet():
    print("Hello")
    print("Data Engineering Track")


greet()  # Calling/Invoking/Firing/Executing
# Jump and Return

# ---------------------------------------------------------


# 2. With Positional Parameters, No Return
def greet_with_name(name_parameter):  # Parameter (Temp Variable/Placeholder)
    print("Hello,", name_parameter)


# Calling/Invoking/Firing/Executing
greet_with_name("Veronia")  # Argument (Value)
greet_with_name("Eman")  # Argument (Value)


# Can't access function's parameter outside function
# print(name_parameter)  # Name "name_parameter" is not defined

# ---------------------------------------------------------


# 3. No Positional Parameters, with Return
# Capture return (Assignment - Print)
def greet_with_return():
    return "Hello, DE Track"


# print(greet_with_return())

# result = "Hello, DE Track"
# print(result)

# ---------------------------------------------------------


# 4. with Positional Parameters, with Return
def add(x, y):  # x = 1, y = 2
    result = x + y  # 1 + 2 = 3
    return result  # Destruction all variables and parameters inside function
    # temp_variable = 3 ❌ after delivering temp_variable, destructed


addition = add(1, 2)
print(addition)


# add()  # Without Arguments
# Missing positional arguments "x", "y" in call to "add"

# ---------------------------------------------------------


# Default Parameter
def greet_with_defaults(name="Guest"):
    print("Hello,", name)


# Without Args
greet_with_defaults()
# With Args
greet_with_defaults("Abdulla")


# Positional Parameters first, then Default Parameters
# def f1(name="Guest", age):  # parameter without a default follows parameter with a default
#     pass


def f1(
    age,
    name="Guest",
):
    pass


# ---------------------------------------------------------


# Star-args / Splat operator => *args
# Variable Number of Positional Arguments
def total(*args):
    # args = (1,2,3,4,5) immutable array (Tuple)
    return sum(args)


print(total(1))
print(total(1, 2))
print(total(1, 2, 3))
print(total(1, 2, 3, 4))
print(total(1, 2, 3, 4, 5))


# Positional Parameters first, then Default Parameters, then *args

# ---------------------------------------------------------

# Strings
str1 = "Hello, "
str2 = "Eman"

# Concatenations +
print(str1 + str2)

# ---------------------------------------------------------


def fullname(*args):
    fullname = ""
    for i in args:
        fullname += i + " "
    return fullname


print(fullname("Hassan", "Mohamed", "Hassan", "ELDash"))


def display(*words):
    for word in words:
        print(word)


display("Python", "Java", "JS", "Kotlin")


def show_items(category, *items):
    print("Category: " + category)
    print("Items:")
    for item in items:
        print(item)


show_items("Electronics", "Laptop", "Smartphone", "Tablet", "TV", "Iron")


def total_price(*prices):
    total = 0
    for i in prices:
        total += i
    return total


print(total_price(15, 200, 305, 410, 25))

# ---------------------------------------------------------
# Dictionary
products = {
    "Grocery": 250,
    "Eggs": 160,
    "Milk": 35,
    "Fruits": 150,
}


# Double Splat Operator => **kwargs: variable keyword arguments (dict)


def display_info(**kwargs):
    for key, value in kwargs.items():
        print(key, "->", value)


display_info(name="Ali", age=30, city="Aswan")


def show_student_info(name, *items, **grades):
    print("Name:", name)
    print("Items:")
    for i in items:
        print(i)

    for key, value in grades.items():
        print(key, "->", value)


show_student_info(
    "Eman", "Pencel", "HandBag", "Eraser", "Pen", "Ruler", Python=100, Data_Science=99
)


# ---------------------------------------
# 14. Scope:
# ---------------------------------------
# where a variable is accessible
# 1. Local => inside function
# 2. Global => Defined at top-level of the code/script
# 3. Built-in => len(), print(), max(), sum()
# 4. Enclosed => Nested Functions


def outer_function():  # Outer Function
    outer_variable = 15

    def inner_function():
        inner_variable = 10
        print(outer_variable)

    inner_function()


outer_function()

# ---------------------------------------------------------


# Closures
def outer_function_enclosures():  # Outer Function
    outer_variable = 15

    def inner_function_enclosures():
        inner_variable = 10
        print(outer_variable)

    return inner_function_enclosures


_enclosures = outer_function_enclosures()


_enclosures()

_enclosures()


def power_factory(n):
    def power(x):
        return x**n

    return power


square = power_factory(2)  # def power(x): return x**2
print(square(3))

cube = power_factory(3)  # def power(x): return x**3
print(cube(2))

# function can't modify variable from outside function

count = 0  # Global Variable


def increment():
    global count
    count += 1  # UnboundLocalError: cannot access local variable 'count' where it is not associated with a value


increment()

print(count)

increment()

print(count)


count += 5


def counter():
    count = 0

    def inc():
        nonlocal count
        count += 1
        return count

    return inc


increase_counter = counter()

print(increase_counter())
print(increase_counter())
print(increase_counter())
print(increase_counter())
print(increase_counter())
print(increase_counter())


# SOLID Principles => Clean Code
# Open for Extension, Closed for Modification
# ---------------------------------------------------------

# Decorator: Functions take another function/code as input, add or modify its behavior, or add add metadata, and return a new function --- without modifying original code


# Manual Decorator Structure (Classical)
# original code/function
def hello():
    print("Hello")


def my_decorator(original_function):
    def wrapper():
        print("Before the original_function")
        original_function()
        print("After the original_function")

    return wrapper


# hello()


# decorated = my_decorator(hello)
# decorated()


# Python Shortcut syntax with @
@my_decorator
def say_hello():
    print("Hello after decorator")


say_hello()


import time


# Timing Decorator
def timer_decorator(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Time Taken:", end - start)

    return wrapper


@timer_decorator
def slow_function():
    time.sleep(1)
    print("Finished")


slow_function()

# ---------------------------------------------------------


# Return Multiple values
def numbers_():
    num1 = 100
    num2 = 500
    num3 = 1000
    return num1, num2, num3  # Tuple (immutable array)


print(numbers_())

# ---------------------------------------------------------

# unpacking/destructuring tuple
a, b, c = numbers_()

print(a)
print(b)
print(c)

# a1, b1 = numbers_() # ValueError: too many values to unpack (expected 2, got 3)

# star or asterisk not only used in function's parameters list, but also in unpacking techniques

list1 = [1, 2, 3]
list2 = [4, 5, 6]
joined_list = [*list1, *list2]
print(joined_list)
# Output: [1, 2, 3, 4, 5, 6]

# ---------------------------------------------------------

# lambda (Anonymous Function)


# Regular/Traditional Function
def square_function(x, n):
    return x**n


square_variable = lambda x, n: x**n
print(square_variable(5, 2))

# ---------------------------------------------------------

# Type Hints: (Readable), Python v3.5
age1: int = 33


def add_func(x: int, y: int) -> int:
    return x + y


# ---------------------------------------------------------


# Documentation
def say_goodnight():
    """
    This Function the user uses to print Goodnight
    """
    print("Goodnight")


print(say_goodnight.__doc__)  # __ => dander

# ---------------------------------------
# 15. Data Structure:
# ---------------------------------------
# String (str): ordered, Zero-based indexing, immutable sequence of characters
string1 = "Hello Data Engineering."  # index = order - 1
# Space indexed as a character

print(string1[0])
# string1[0] = 'D' # Unsupported target for indexed assignment ("str")

print(string1[-1])  # Negative Index

# Slicing
print(string1[0:2])  # Exclude Final Index (Slicing)

print(string1[:2])  # Omit start Index

print(string1[1:])  # Omit final Index

print(string1[:])  # Omit start, final Index

# step by default 1
print(string1[::2])  # Omit start, Omit final Index, step = 2

# Reverse String
print(string1[::-1])  # Omit start, final Index, step = -1


# Built-in Functions/Methods
# len(sequence) => return length (Spaces Included)
print(len(string1))


# .count("Characters") => Case-Sensitive
print(string1.count("e"))


# .capitalize()
print(string1.capitalize())


# .upper()
print(string1.upper())


# .lower()
print(string1.lower())


# .replace("replaced/deleted element", "replace by this element")
print(string1.replace("ll", "@"))


string2 = "         ABC           "

# .lstrip() => remove leading whitespaces
print(string2.lstrip())

# .rstrip() => remove trailing whitespaces
print(string2.rstrip())

# .strip() => remove leading and trailing whitespaces
print(string2.strip())

# .center(Number of characters, "Characters") => center text
print(string2.strip().center(50, "*"))

string3 = "a b c d e"

# .split("sep") => return array/list
print(string3.split(" "))


# .find("Characters")
print(string1.find("z"))  # index of first occurrence => if not found return -1

# .startswith('expression') => return bool
print(string1.startswith("Hello"))  # True

# .endswith('expression') => return bool
print(string1.endswith("Hello"))  # False

# sequence.index(element, start, end)

# in => check existence in a string => return bool
print("l" in "Hello")

# Concatenation
print("Hello" + "!")

# Interpolation
str1 = "Hello "
str2 = "DE"
print(str1 * 2 + str2)


# Special Character \n \t \\ \" \' \r \b

# Formatted String
name = "Hassan"

# f-string
print(f"Hello {name}!")


# # .format(variable1, variable2)
# message = "She is {0}, and she graduated from {1}"
# print(message.format("Eman", "CS"))

# message1 = "She is {n}, and she graduated from {f}"
# print(message.format(n="Eman", f="CS"))


# .isalpha() => All characters are alphabet => True, otherwise False
x1 = "Abdo1"
print(x1.isalpha())


# .isdecimal() => All characters are digits => True, otherwise False
x1 = "123a"
print(x1.isdigit())
# Standard Digits (0, 1, 9) Only
# But Don't Accept Superscripts/Subscripts (², ³, ₀), Circled Numbers (①, ⑳), Vulgar Fractions (½, ¼, ¾), Roman Numerals (Ⅰ, Ⅻ), Currency/Decimals ($, ., ,)

# .isdigit() => All characters are digits => True, otherwise False
x1 = "123a"
print(x1.isdigit())
# Standard Digits (0, 1, 9), Superscripts/Subscripts (², ³, ₀), Circled Numbers (①, ⑳)
# But Don't Accept Vulgar Fractions (½, ¼, ¾), Roman Numerals (Ⅰ, Ⅻ), Currency/Decimals ($, ., ,)


# .isnumeric() => All characters are digits => True, otherwise False
x1 = "123"
print(x1.isnumeric())  # More General (Broadest)
# Standard Digits (0, 1, 9), Superscripts/Subscripts (², ³, ₀), Circled Numbers (①, ⑳), Vulgar Fractions (½, ¼, ¾), Roman Numerals (Ⅰ, Ⅻ)
# But Don't Accept Currency/Decimals ($, ., ,)
# .isupper()
x1 = "ITi"
print(x1.isupper())

# .islower()
x1 = "iti"
print(x1.islower())


# ---------------------------------------------------------

# Numbers (int, float, complex)
a, b, c, d, e = 1000, 5000, 3666, 26.16, 30.55

# min(variables)
print(min(a, b, c, d, e))


# max(variables)
print(max(a, b, c, d, e))


# round(variable)
print(round(d))
print(round(e))


# complex numbers
complex1 = 4 + 5j
complex2 = complex(4, 5)

print(type(complex1))
print(type(complex2))

# ---------------------------------------------------------
# Lists (Array in other languages): [_, _, _], Zero-based indexing, mutable, Elements from different types
items = ["Milk", "Eggs", "Fruits", "Vegetables"]

print(items)

items[0] = "Grocery"
print(items)

# Cast any type to list
# list()
print(list(range(5)))


# Built-in Methods (mutating - non-mutating)
numbers_list = [1, 20, 34, 40, 15, 63, 7, 8, 9, 10]

# .sort() => mutating method (Modify Reference)
print(numbers_list)
print(numbers_list.sort())  # None
print(numbers_list)
print(numbers_list.sort(reverse=True))  # None
print(numbers_list)

alphas = ["A", "B", "C", "Z", "S", "a", "b", "64"]
print(alphas)
print(alphas.sort())  # None
print(alphas)


# .reverse() => mutating method (Modify Reference)
alphas = ["A", "B", "C", "Z", "S", "a", "b", "64"]
print(alphas)
print(alphas.reverse())  # None
print(alphas)


# .remove(value) => mutating method (Modify Reference)
print(numbers_list)
print(numbers_list.remove(63))  # None
print(numbers_list)


# .pop() or .pop(index) => mutating method (Modify Reference)
print(numbers_list)  # [40, 34, 20, 15, 10, 9, 8, 7, 1]
print(numbers_list.pop())  # 1
print(numbers_list)  # [40, 34, 20, 15, 10, 9, 8, 7]
print(numbers_list.pop(5))  # 9
print(numbers_list)  # [40, 34, 20, 15, 10, 8, 7]

# .append(item) in the end => mutating method (Modify Reference)
print(items)
print(items.append("Candy"))  # None
print(items)


# .insert(index, value) => mutating method (Modify Reference)
print(items)
print(items.insert(0, "Cheese"))  # None
print(items)


items2 = ["Rice", "Bananas"]

# .extend(list) => mutating method (Modify Reference)
print(items.extend(items2))  # None
print(items)

# separator.join(words)
words = ["Python", "is", "fun"]
separator = " "
result = separator.join(words)
print(result)  # Output: Python is fun

items2 = ["Rice", "Bananas", "Rice"]
print(items2)
print(items2.remove("Rice"))  # remove first occurrence
print(items2)

# List Concatenation => non-mutating method
print(numbers_list + items)
print(numbers_list)
print(items)

# len(sequence)
print(len(numbers_list))  # no of items
# last index = len(sequence) - 1

# Search for Membership (in) => Case-Sensitive
print("eggs" in items)

# sequence.index(element, start, end)

# min(sequence)
print(min(numbers_list))


# max(sequence)
print(max(numbers_list))


# Looping over List (items/values)
for i in items:
    print(i)

# Looping over index, items in the same list
print(enumerate(items))  # <enumerate object at 0x000001E5D2ADE840>

for index, item in enumerate(items):
    print(f"{index} -> {item}")

fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")


# Looping over two separate lists

names = ["Veronia", "Ali", "Eman", "Soha"]
ages = [20, 35, 20, 19]

print(zip(names, ages))  # <zip object at 0x00000167919A9480>


for i, j in zip(names, ages):
    # print(f"{i} is {j} years old")
    print(i, "is", j, "years old")


# ---------------------------------------------------------

# Tuples (_, _, _): Ordered, Zero-indexed - Immutable
t = (6, 5, 2)

print(t)
print(t[0])

# t[0] = 15  # Unsupported target for indexed assignment ("tuple[int, int, int]")

# Cast to tuple
t1 = tuple(numbers_list)
print(t1)

# Cast tuple to list
tuple_as_list = list(t)
print(tuple_as_list)


# len(sequence)
print(len(t))


# min(sequence)
print(min(t))


# max(sequence)
print(max(t))


# Search for Membership (in) => Case-Sensitive
print(1 in t)

# Tuple from one element (ended with ,)
tup1 = ("Apple",)
print(tup1)

# sequence.index(element, start, end)

# del
del tup1
# print(tup1) # NameError: name 'tup1' is not defined. Did you mean: 'tuple'?

# Looping over tuple
for i in t:
    print(i)

# ---------------------------------------------------------

# Sets {_, _, _}: unordered (No Index), mutable, unique elements, no duplication

s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 6, 3, 7}
print(s)

# print(s[0])  # TypeError: 'set' object is not subscriptable

print(list(s))

print(set(numbers_list))

# Built-in Methods

# .add(item)
s.add(1)
print(s)

s.add(10)
print(s)

# .remove(value)

s.remove(8)
print(s)

# .clear()
s.clear()
print(s)  # set()


# .union(set) => non-mutating method
s1 = {20, 30}
s2 = {16, 13, 20}

new_set = s1.union(s2)
print(new_set)


# .difference(set)
unique_set = s1.difference(s2)
print(unique_set)


# .intersection(set)
repeated_set = s1.intersection(s2)
print(repeated_set)


# print(s + unique_set) # TypeError: unsupported operand type(s) for +: 'set' and 'set'
print(s1 | s2)  # union
print(s1 - s2)  # difference
print(s1 & s2)  # intersection
print(s1 ^ s2)  # symmetric difference

# ---------------------------------------------------------

# Dictionary: { "key1": "value1", "key2": 1 } key-value pairs - key(index) is immutable and unique


dict1 = {
    "Ahmed": 20,
    "Alaa": 50,
    "Omar": 22,
    "Lamyaa": 20,
    "Ahmed": 50,  # overwrite old value
}

print(dict1)


# .get(key)

print(dict1.get("Omar"))


# .pop(key)
print(dict1.pop("Omar"))
print(dict1)


dict1["Ahmed"] = 35
print(dict1)

# .update(dictionary)

dict1.update({"Alaa": 44})
print(dict1)

# .keys() => dict_keys(['Ahmed', 'Alaa', 'Lamyaa'])
print(dict1.keys())
print(list(dict1.keys()))

# .values()
print(dict1.values())
print(list(dict1.values()))


# Membership
print("Hassan" in dict1)


# Looping
# Python 3.6 => Dictionaries is unordered
# Python 3.7+ => Dictionaries is ordered

# Iterate over keys: Python 3.7+
for i in dict1:
    print(i)

# Iterate over keys: Python 3.6-
for i in dict1.keys():
    print(i)


# Iterate over values:
for i in dict1.values():
    print(i)


# Iterate over items:
for i in dict1.items():
    print(i)


# ---------------------------------------
# 16. List Comprehensions:
# ---------------------------------------

# list_numbers = [0, 1, 2, 3, 4, 5]
# list_numbers = []
# for x in range(6):
#     list_numbers.append(x)


# List_Comprehensions = [expression for item in iterable]

list_numbers = [x for x in range(6)]

# squares 0 to 4
squares = [x**2 for x in range(5)]
print(squares)

# Adding a condition (if)
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers_list if x % 2 == 0]
print(evens)


numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
labels = ["Even" if x % 2 == 0 else "Odd" for x in numbers_list]
print(labels)


nums_list = [x + 1 for x in range(10)]
print(nums)

cities = ["caIro", "giZa", "beniSUef", "Minya", "faYoum", "aLex", "aSSuit", "aSWan"]
capitalized_cities = [i.capitalize() for i in cities]
print(capitalized_cities)

filtered_cities = [x.capitalize() for x in cities if x[0] != "a"]
print(filtered_cities)


sports = ["fOOtball", "haNdbAll", "bAsKetbaLl", "Tennis", "Golf", "VallyBall"]
chosen_sport = [sport.capitalize() for sport in sports if "ball" in sport.lower()]
print(chosen_sport)
# ---------------------------------------
# 18. Higher Order Functions, Callback Functions:
# ---------------------------------------
# Higher Order Functions: Functions take another functions as arguments
# Callback Functions: Functions as arguments for another functions
items = ["GrocEry", "MiLk", "EgGs", "FrUiTs", "VegeTAbles", "ChEEse", "MaYo"]


# def capitalize(words):
#   return word.capitalize()

# map(function, iterable)
capitalized_items = list(map(lambda word: word.capitalize(), items))
# <map object at 0x000001DE90BDC880>
print(capitalized_items)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
doubled_numbers = list(map(lambda n: n * 2, numbers))
print(doubled_numbers)

# filter(function, iterable)
items = ["Grocery", "Milk", "Eggs", "Fruits"]
filtered_items = list(filter(lambda item: len(item) == 4, items))
# <filter object at 0x0000014E742A8CA0>
print(filtered_items)

filtered_items = list(filter(lambda item: item[0] != "M", items))
print(filtered_items)

prices = [250, 99, 550, 3500, 450, 50]
filtered_prices = list(filter(lambda price: price < 100, prices))
print(filtered_prices)


products = {
    "Grocery": 250,
    "Milk": 30,
    "Eggs": 240,
    "Fruits": 550,
    "Vegetables": 300,
    "Cheese": 450,
    "Mayo": 550,
}

print(list(products.items()))

filtered_products = dict(filter(lambda item: item[1] > 100, products.items()))
print(filtered_products)


# ---------------------------------------
# 19. Error Handling:
# ---------------------------------------
# Errors/Exceptions Types:

# ZeroDivisionError
# print(10 / 0)  # ZeroDivisionError: division by zero


# TypeError
# total = "abc" + 5 # TypeError: can only concatenate str (not "int") to str


# ValueError
# age = int("twenty") # ValueError: invalid literal for int() with base 10: 'twenty'


# IndexError
# numbers = [1, 2, 3]
# print(numbers[5]) # IndexError: list index out of range


# KeyError
person_dict = {"name": "Hassan"}
# print(person_dict["age"]) # KeyError: 'age'

# ModuleNotFoundError/ImportError
# import non_existing_library  # ModuleNotFoundError: No module named 'non_existing_library'


# AttributeError
name = "python"
# name.append("3")  # AttributeError: 'str' object has no attribute 'append'

# FileNotFoundError
# file = open("Notes.txt", "r")


# IndentationError => Interrupt Interpreter
# def hi():
# print("Hi") # IndentationError: expected an indented block after function definition on line 1664


# SyntaxError => Interrupt Interpreter
# def hi() # SyntaxError: expected ':'
#     print("Hi")


# Error Handling:
# try - except - else - finally

# try:
#     # code
# except Error:
#     # Recovery Code


try:
    print(10 / 0)
    # age = int("twenty")
    # print("Hello")

# except ZeroDivisionError:
#     print("Zero Division Error")

# except ValueError:
#     print("Value Error")

except Exception as e:
    print("Error:", e)


# else:
#     print("No Error Found")

finally:
    print("Always run")


print("Normal Flow")


# # Raise Exception
# x = int(input("Enter Positive Number: "))

# if x < 0:
#     # raise ValueError("Number must be Positive!")
#     raise Exception("Number must be Positive!")


# ---------------------------------------
# 20. File Handling:
# ---------------------------------------
# Open - Create - Read - Write - Append - Delete
# Text Files -> .txt, .csv, .json, .py
# Binary Files -> images, videos, .zip, .7z, .rar, .exe, .bat


# Open Files:
# file = open("file_name", "mode")
# file = open("Notes.txt", "r") # FileNotFoundError: [Errno 2] No such file or directory: 'Notes.txt'

# modes:
# 'r' - Read - Open existing file for Reading Only - Fails if file not found
# 'w' - Write - Create or overwrite the file - Clear all Content
# 'a' - Append - Add content to the end of file - Create if file not found
# 'x' - Exclusive - Create new file, Fails if file exists
# 'b' - Binary - use with other for Binary Files
# '+' - Read/Write - 'r+' or 'w+'


# Read file Line by Line
file = open("Notes.txt", "r")
for line in file:
    print(line.strip())
print(file)  # <_io.TextIOWrapper name='Notes.txt' mode='r' encoding='cp1256'>
file.close()


# Read Whole File at once
file = open("Notes.txt", "r")
content = file.read()
print(content)
file.close()


# Read Whole Line by Line into List
file = open("Notes.txt", "r")
lines = file.readlines()
print(lines)
file.close()


# Write to file (Overwrite)
file = open("Notes.txt", "w")
file.write("Hello from Write Mode")
file.close()

# Append to file
file = open("Notes.txt", "a")
file.write("\nHello from Append Mode")
file.close()


# with statement - Automatic File Closing
with open("Notes.txt", "r") as file:
    content = file.read()
print("After Closing:", content)


import csv

with open("1.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


import json

with open("1.json", "r") as file:
    data = json.load(file)

print(data)

# Task: Difference between load vs loads

products = {
    "Grocery": 250,
    "Milk": 30,
    "Eggs": 240,
    "Fruits": 550,
    "Vegetables": 300,
    "Cheese": 450,
    "Mayo": 550,
}

with open("1.json", "w") as file:
    json.dump(products, file, indent=4, sort_keys=True)

# [
# 	{
# 		"name": "Hassan",
# 		"age": 33
# 	},
# 	{
# 		"name": "Alaa",
# 		"age": 23
# 	}
# ]


# Serialization/Stringification Dictionary
# Convert Dictionary/Python Object to string
# json.dump(products, file, indent=4, sort_keys=True)

# Deserialization/Parsing
# Convert string to Dictionary/Python Object
# json.load("file.json")

# str_dict = str(dic1)
# print(str_dict) # Not JSON Standard (Single Quoted)
# str_dict = str(dic1)
# print(str_dict) # Not JSON Standard (Single Quoted)
# print(type(str_dict))

# print(
#     dict(str_dict)
# )  # ValueError: dictionary update sequence element #0 has length 1; 2 is required

# dict_items = [("Hassan", 33), ("Mohamed", 26)]

# print(dict([("Hassan", 33), ("Mohamed", 26)]))


# Normal Casting Failed to Convert dict to JSON or From JSON to dict
# To deal with JSON => Use First Party Library (json)
# import json

# converted_json = json.loads(str_dict)
# print(converted_json)


# ---------------------------------------
# 20. Modules:
# ---------------------------------------
# Every py file is a module we can import any any piece of code from it into another file

# Built-in Modules in Python
import math
import random
import time
import datetime
import os
import sys
import csv
import json


print(random.randint(1, 10))
print(random.choices(["a", "b", "c"]))

print(math.sqrt(16))
print(math.pi)


# Partial Import
from math import acos, acosh


# Aliasing
import math as m


# User-defied Module
import new

print(new.hello())

# Package: folder has many modules can imported => empty fil named __init__.py

from my_package.auth import authorization


# if run directly
print(__name__)  # __main__


# if run file from import statement
print(__name__)  # file_name


def main():
    return "All File Logic"


if __name__ == "__main__":
    print("File run directly from terminal")
    main()


# External (3rd Party) Libraries / Packages / Modules
# upload on The Python Package Index (PyPI) is a repository of software for the Python programming language.
# pip: package installer (Manager)
# install package globally


# Virtual Environment
# 1. Create Virtual Environment: Terminal => python -m venv .venv
# 2. Activate Virtual Environment:
# Terminal on Windows => .venv\Scripts\activate
# Terminal on Linux => source .venv/Scripts/activate

# pip install numpy

import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(array)


# Data Visualization => matplotlib

import matplotlib.pyplot as plt

horizontal = np.arange(0, 11, 1)
# print(list(horizontal))

vertical = horizontal**2


# plt.plot(horizontal, vertical)
# plt.title("Y - X Exponent")
# plt.xlabel("X values")
# plt.ylabel("Y values")
# plt.show()

# import psycopg2

# connection = psycopg2.connect(
#     host="localhost", port="5432", database="sql_lab_one", user="test", password="test"
# )

# print("Database Connected Successful ✅")

# # Create a cursor to execute SQL commands
# cursor = connection.cursor()

# # Execute simple SQL command
# cursor.execute("SELECT version();")


# # Fetch One Result
# version = cursor.fetchone()
# print("PostgreSQL Version:", version[0])


# cursor.execute(
#     """
#         CREATE TABLE students (
#             id SERIAL PRIMARY KEY,
#             name VARCHAR(100),
#             grade INTEGER
#         );
#     """
# )
# print("Table Created Successful ✅")

# cursor.execute("SELECT * FROM employee;")
# rows = cursor.fetchall()

# for row in rows:
#     print(row)

# # Save Changes
# connection.commit()

# cursor.close()
# connection.close()


import requests

url = "https://fakestoreapi.com/products"
response = requests.get(url)


print("Status Code: ", response.status_code)
print("Response as dict: ", response.json())
print("Response as raw: ", response.text)

# ---------------------------------------
# 21. OOP:
# ---------------------------------------
# Paradigm:
# Procedural Programming
# Functional Programming
# Event-Driven Programming
# Object-Oriented Programming (OOP)

# Classes => Blueprint/Template
# Properties/Attributes/Data Members/Instance Member/Instance Data/Instance Variable
# Methods/Actions/Behaviors/Functions inside Class


# New/User-Defined Data Type
class Person:
    # pass
    # Class Attribute
    pi = 3.14  # Shared across all objects
    x

    # Constructor => used once when creating new object only
    def __init__(self, n, a):
        self.name = n  # Instance/Object Attribute
        self.age = a

    def intro(self):
        self.age = 15
        self.name ='hassan'
# hard coded constructor


    # Instance/Object Method
    def intro(self):
        print(f"This is {self.name}, Age is {self.age}")

        # class method  ==> access or modify class states
        # @ class method
        @classmethod
        def method_name(cls,parameter):
            pass
        
        
        
        # static method  ==> unbonded => validator , formatters , converters
        @staticmethod
        def emai_is_valid(email):
            return '@' in email and '.' in email
        emai_is_valid('menashafik@gmail.com')
            
# Missing Methods Types
# Constructor

# Constructor: Special Function, when creating new object, initialize attributes
# self: refer current object/instance => Java/C++(this)
# self must be the first parameter of all method


# Objects: Different Instances
p1 = Person("Hassan", 33)
print(type(p1))

# print("X:", Person.x) # "type[Person]" has no attribute "x"
# print("Not Yet Defined", Person.name) # AttributeError: type object 'Person' has no attribute 'name'

# Access Object Attributes/Methods => dot operator
print(p1.name)

p1.name = "Ahmed"

p1.intro()


# Class Attribute
print(p1.pi)  # can be accessed from object
print(Person.pi)  # can be accessed directly from class


# OOP: 4 Pillars
# Inheritance  ==> reusability (DRY , SOLID)
# Parent == super class == base class
# child == derived == sub class
# child inherits all methods/attributes from parent

class Animal:
    legs = 4
    def __init__(self,name):
        self.name = name
    def speak(self):
        print('sound')

class Dog(Animal):
    def speak(self):
        print('barking')


# Polymorphism  ===> reusability ( --- overload)

# overriding == 


# Encapsulation
# bundle / encapsulate data and logic in the class
# hide internals (access modifier /specifiers)
# access hide internal (setters / getters)

class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self._balance = balance
        self.__pin = '1234'
    
    def statment(self):
        print(f"account_holder is{self.account_holder} | balance is {self._balance}")
        
    def __display_pin(self):
        print(f"secret pin is {self.__pin}")
        
        
# class childAcount(BankAccount):
#     def __init__(self,account_holder,balance,allowance):
#         self.account_holder = account_holder
#         self._balance = balance
#         self.__pin = '1234'
    
#     def statment(self):
#         print(f"account_holder is{self.account_holder} | balance is {self._balance}")
        
        # access modifiers/specifiers
        # defualt => public => accessable anywhere 
        # proteced => internal use,childs => self._balance <==
        # ptivate  =>intenal use only  => mangling ==> self.__balance

# Abstraction
