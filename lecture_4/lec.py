# list_num = [0,1,2,3,4,5,6]

# list_num =  []
# for i in range(7) :
#     list_num.append(i)
    
# print(list_num)
# ===========================================
# list comperhensions
# ===========================================

# list_num = [ex for item in iterable]

# list_number = []

# list_number = [i for i in range(6)]
# print(list_number)
# squares 0 to 4
# squares = [i**2 for i in range(5)]
# print(squares)

# even numbers 
# list_number = [1,2,3,4,5,6,7,8,9,10]

# even = [i for i in list_number if i%2 == 0]
# print(even)

# labels = ["even" if x % 2 == 0 else "odd" for x in list_number]
# print(labels)

# ===========================================
# higher order functions:
# ===========================================
# items = ["GrocEry","Milk",'EGgs','FrUiTs']

# capitalize = map(lambda word:word.capitalize(),items) #<map object at 0x00000248D645B780>
# list_m = list(capitalize)
# print(list_m)

# double = list(map(lambda n:n*2,list_number))
# print(double)

# filter_item = list(filter(lambda n:len(n)==4,items))
# print(filter_item)

# princes = [250,124,146,78,2500,1245,5]

# filter_prices = list(filter(lambda n : n <=100,princes))
# print(filter_prices)

prod ={
    
    "grocery":1500,
    "milk":30,
    "eggs":150,
    "fruits":50,
}

# filter_prod = dict(filter(lambda i : i[1] > 100,prod.items()))
# print(filter_prod)

# ===========================================
# exceptions & errors handling
# ===========================================

# print(10/0) #ZeroD

# total = 'abc' + 5
# print() TypeError: can only concatenate str (not "int") to str
# age = int("tin")
# ValueError: invalid literal for int() with base 10: 'tin'
# print('narmal flow')
# m = [1,2,4]
# IndexError: list index out of range
# print(m[5])

# pre = {'name':'hassan'}
# print(pre['mak'])
# KeyError: 'mak'

# import non ModuleNotFoundError: No module named 'non'
# name ='python'
# name.push("3")
# AttributeError: 'str' object has no attribute 'push'

# try - except - else 0 finally

# try:
    
# except KeyError:
    # recovery code
    
# try:
#     print(10/0)
#     age =int('kldn')
# except ZeroDivisionError:
#     print('you should not devide on 0')
# except ValueError:
#     print('value error')
    
# except Exception as e:
#     print("error : ",e)
    
# Raise Exeption 
# x = int(input('Enter positive numbers: '))

# if x < 0:
#     raise ValueError('you are crazy !')

# ===========================================
#  files access handling
# ===========================================
# create - open - write - append - delete
# text files .txt , .csv , .json
# binary files -> .images , .videos , .zip , .rar,.7z , .exe

# file = open("file name","mode")
# modes:
# 'r' - read -open
# file = open("notes.txt","r") #ValueError: invalid mode: 'mode'
# 'w' write - create or overwrite the file - clear all content
# "a" append - add content to the end of the file - create if file not found
#  "x" exclusive - create new file , fails if file exists 
# "b" binary - use with binary files format
# "+" read/write - 'r+' or 'w+'

# files = open("notes.txt","r")
# for line in files:
#     print(line)
# files.close()

# read whole file at once
# file = open("notes.txt","r")
# content = file.read()
# print(content)
# file.close()


# read whole file at once abd conver to a list 
# file = open("notes.txt","r")
# lines = file.readlines()
# print(lines)
# file.close()

#write in the file  

# file = open("notes.txt","w")
# file.write("hello mina , you are a data engineer !")
# file.close()

# append

# file = open("notes.txt","a")
# file.write("\nfrom append !")
# file.close()

# with statement - automatic file closing

# with open("notes.txt","r") as file:
#     content = file.read()
# print(content)

# import csv
# with open("book.csv","r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)
        
        
import json
# with open("1.json","r") as file :
#     data = json.load(file)
#     print(data)
    
    # task is the difference between load , loads
   
# json.load() → works with files

# Think load = load from file

# Input: a file object

# Used when JSON is stored in a .json file

# json.loads() → works with strings

# Think loads = load from string

# Input: a string

# Used when JSON comes from API response, text, variable, etc.

with open("1.json","w") as file :
    data = json.dump(prod,file,indent=4,sort_keys=True)

# serialization / stringification

# ===========================================
# modules :
# ===========================================

# built in liberaries 
# import math
# import random
# import time
# import os
# import sys
# print(time.time())
# import datetime


# sys -- os
# print(random.randint(1,15))

# print(math.sqrt(16))
# print(math.pi)

# partial import 
# from math import pi,acos
# aliasing
# import math as m 


# import new 
# print(new.hello('mina'))
# from my_package.auth import x
# print(x)


# import numpy as np 

# import matplotlib.pyplot as plt

# horiz = np.arange(0,11,1)
# print(horiz)
# ver = horiz/2
# plt.plot(horiz,ver)
# plt.show()


# import psycopg2
# connection = psycopg2.connect(
#     host = "localhost",port='5432',database="sql_lab_one",user='test',password='test'

# )
# print('data connected')

# cursor = connection.cursor()

# cursor.execute('select vession();')
# connection.commit()
# cursor.close()
# connection.close()


# ===========================================
# OOP 
# ===========================================
# paradigm
# procedural programming
# functional programming 
# event-driven programming
# GUI

# classes ==>  Blueprint/ (structure) / templete
# properties ==> attributes / data members / instanse member / instance variable
# methods ==> actions / behaivior / function inside class


class Person:
    # age
    def __init__(self):
        pass
    def intro(self):
        self.age = 15
        
        
# constructors  special function

def __init__(self,n,a):
    self.name = n #init - declare
    self.age = a
# objects different instances

p1 = Person("hassan",33)

print(type(p1))