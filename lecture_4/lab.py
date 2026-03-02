# Topics: *args, **kwargs, default parameters
# Define a function `student_score(name, *grades, bonus=0)`
# It should:
# 1. Print student name
# 2. Calculate average of grades
# 3. Add the bonus to the average if provided
# 4. Print final result like: "Ali's score is 85.5"
# ✅ Try calling with:
# student_score("Ali", 90, 80, 85)
# student_score("Sara", 88, 79, 95, bonus=5)

# ===========================================
# def student_score(name,*grades,bonus=0):

#        avg= round(sum(grades)/len(grades),2)
#        final_score = avg + bonus
#        print(f"the name is : {name}")
#        print(f"the average grade before the bonus is : {avg}")
#        print(f"the average grade after the bonus is : {final_score}")
#        print(f"{name}'s score is {final_score}")
        
# student_score("Ali", 90, 80, 85)
# student_score("Sara", 88, 79, 95, bonus=5)

# ===========================================
# 📁 Topics: Nested functions, closures, scope
# # Create a function `discount_calculator(rate)` that returns another function `apply(price)`
# # That inner function returns price after applying discount

# ===========================================

# def discount_calculator(rate):
#     def apply(price):
#         return price - (price * rate)
#     return apply

# ten_percent = discount_calculator(0.10)
# print(ten_percent(200))

# ===========================================

# 📁 Topics: Decorators, functions, dict
# Write a decorator `@check_authentication` that:
# - Accepts a dictionary `user` with keys "name" and "Authenticated"
# - Allows function to run if Authenticated is True
# - Else prints: "Access Denied"

# Apply it to a function `access_portal(user)`
# ✅ Sample user:
# {"name": "Ahmed", "Authenticated": False}

# ===========================================
# def check_authentication(fun):
#     def wrapper(user):
#         if user.get("Authenticated"):
#             return fun(user)
#         else:
#             print("access denied")
#     return wrapper
        
# @check_authentication
# def access_portal(user):
#     print(f"welcome {user['name']} ! You can access the portal.")
    
# user1 = {"name": "Ahmed", "Authenticated": False}
# user2 = {"name": "Sara", "Authenticated": True}

# access_portal(user1)
# access_portal(user2)
# ===========================================

# Topics: return multiple values, unpacking
# Write a function `get_user_location()` that returns:
# country, city, postal_code

# Call the function, unpack the values, and print:
# "You are located in Cairo, Egypt. Zip: 12345"
# ✅ Bonus: Try unpacking into 2 vars and handle the error with try/except.

# def get_user_location():
#     country = "egypt"
#     city = "cairo"
#     postal_code= 12345
#     return country, city, postal_code
    
# country,city,postal_code = get_user_location()
# print(f"You are located in {city}, {country}. Zip: {postal_code}")

# # # ===========================================

# try:
#     first,second = get_user_location()
# except ValueError as e:
#     print("unpacking error : ",e)
    
# ============================================

# Topics: lambda, sort(), lists
# Given this list:
# products = [("TV", 5000), ("Laptop", 8000), ("Tablet", 3000)]
# # Sort by:
# # 1. Price (ascending)
# # 2. Name length (descending)
# # 3. Alphabetically
# # Print after each sort
# # ============================================
# # 1. Price (ascending)

# price_asc = products.sort(key=lambda x:x[1])
# print(products)

# # ============================================
# # 2. Name length (descending)

# price_asc = products.sort(key=lambda x:len(x[0]),reverse=True)
# print(products)

# # ============================================
# # 3. Alphabetically

# price_asc = products.sort(key=lambda x:x[0])
# print(products)

# ============================================
# Topics: Type hints, error handling
# Write a function `def total_price(price: float, quantity: int) -> float`
# Multiply them and return the result
# If price or quantity is negative, return "Invalid Input"
# ✅ Call the function with both valid and invalid values.

# ============================================
# def total_price(price: float, quantity: int):
   
#     if price < 0 | quantity < 0 :
#         return "invalid number"
#     else:
#         return price * quantity

# print(total_price(-1,5))
# print(total_price(-1,-5))
# print(total_price(1,5))
# ============================================

# Topics: global variable, scope
# Create a global variable `counter = 0`
# Write:
# - increment() to increase counter
# - reset() to set it to 0
# - display() to print current counter
# Call the functions and print output each time

# ============================================

# counter = 0

# def increment():
#     global counter
#     counter+=1
    
# def reset():
#     global counter
#     counter = 0
    
# def display():
#     global counter
#     print('counter is : ',counter)
    
# increment()
# increment()
# display()
# reset()
# display()

# ============================================
# Topics: creating and importing modules
# Step 1: In a new file `math_utils.py`, create:
# def square(n), def cube(n)
# Step 2: In `main.py`, import the functions and test them:
# square(5), cube(3)

# from math_utils import square,cube
# square(3)
# cube(5)

# ============================================

# 🔸 Assignment 9: NumPy Data Processing
# 📁 Topics: NumPy array creation and operations
# Create a NumPy array of even numbers from 0 to 20
# Create a second array that is the square of each element
# Print both arrays side by side

# ============================================

# import numpy as np 

# import matplotlib.pyplot as plt

# val = np.arange(2,21,2)
# print(val)
# sqr = val**2
# # print(sqr)
# plt.plot(val,sqr)
# plt.show()



# ============================================


#  Assignment 10: Matplotlib Graph for Sales
# 📁 Topics: Matplotlib, simple plotting
# x = [1, 2, 3, 4, 5] (Week Numbers)
# y = [200, 450, 300, 500, 700] (Sales in EGP)
# Plot a line graph:
# Title: "Weekly Sales"
# X label: "Week"
# Y label: "Sales (EGP)"

# ============================================

# import matplotlib.pyplot as plt
# x = [1, 2, 3, 4, 5]

# y= [200, 450, 300, 500, 700]
# plt.plot(x, y)
# plt.title("Weekly Sales")
# plt.xlabel("Week")
# plt.ylabel("Sales (EGP)")
# plt.show()

# ============================================


# 📁 Topics: psycopg2-binary, connection, cursor
# Connect to your PostgreSQL database
# SELECT all rows from a table called `courses`
# SQL Command ("SELECT * FROM courses")
# Print each row on a new line
# ✅ Bonus: Use try-except to catch and print connection errors
# ============================================

# import psycopg2

# try:
#     conn = psycopg2.connect(host="localhost",database="mydb",user="test",password="test"
#     )
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM courses")
#     rows = cur.fetchall()
#     for row in rows:
#         print(row)
    
#     cur.close()
#     conn.close()

# except psycopg2.Error as e:
#     print("Database error:", e)
    
# ============================================
# Topics: mysqlclient, connection, cursor
# Instal one of the following libraries:
# pip install mysqlclient or 
# pip install PyMySQL or 
# pip install mysql-connector-python (official/recommended)

# Connect to your MySQL database
# SELECT all rows from a table called `courses`
# SQL Command ("SELECT * FROM courses")
# Print each row on a new line
# ✅ Bonus: Use try-except to catch and print connection errors
# ============================================

# import pymysql

# try:
#     conn = pymysql.connect(host='localhost',user='test',password='test',db='mydb')
#     print('Connection successful!')
#     cursor = conn.cursor()
    
#     cursor.execute("SELECT * FROM courses")
#     rows = cursor.fetchall()
    
#     for row in rows:
#         print(row)

# except pymysql.MySQLError as e:
#     print("Error connecting to MySQL:", e)

# finally:
#     if conn:
#         cursor.close()
#         conn.close()
#         print("Connection closed")

# =============================================0

# Topics: try-except-finally, inputmber
# Divide 100 by the number
# Ask the user to input a nu
# Handle:
# - ZeroDivisionError
# - ValueError (if not a number)

# Use finally to print "Process finished"

# try:
#     num = int(input("Enter a num:  "))
#     result = 100 / num
#     print(f"result is : {result}")
    
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero!")

# except ValueError:
#     print("Error: Invalid input, please enter a number!")
# finally:
#     print("process finished")