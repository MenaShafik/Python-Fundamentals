# dictionary with key and value
person = {'name': "mina",
          "age" : "24"
          }
print((person))

# more info about the product

# prices = {
#     'eggs':150,
#     'fruits':220,
#     'milk':45
# }

# def display_info(**kwargs):
#     for key,value in kwargs.items():
#         print(key,"->",value)
        
        
# display_info(name="mina",age=50,city="soal")


# def show_info(name,*items,**grades):
#     print("name :",name)
#     print("items :",items)
#     for i in items:
#         print(i)
#     for key,value in grades:
#         print(key,value)
        
# show_info(name="mina",items="pincel", items='Handbag',"earser","pen","ruler",python=100,data_sience=120)


# scope
# where a variable is accesible 
# local => inside function
# global => defined at top-level of the code/script
# built in => len() , print() , max() , sum()
# Enclosed => Nested Functions

# def outer_fun():
#     outer_var = 10

    
#     def inner_fun():
#         inner_val = 51
#         print(outer_var)
    
#     inner_fun()
    
# outer_fun()


# enclosure

# def outer_fun_enclosures():
#     outer_var = 10

    
#     def inner_fun_enclosures():
#         inner_val = 51
#         print(outer_var)
    
#     return   inner_fun_enclosures()
    
# _enclosures = outer_fun_enclosures()

# _enclosures()

 # another example

# def counter():
#     count = 0
#     def increase():
#         nonlocal count
#         count+=1
#         return count
#     return increase

# increase_count = counter()
# print(increase_count())



# def power_factor(n):
#     def power(x):
#         return x**n

#     return power

# square = power_factor(4)
# print(square(2))


# count = 0

# def increment():
#     global count
#     count+=1
    
# increment()
# print(count)


# SOLID Principles  as a clean code

# single responselity     
# open for extention -- closed for modification 
# decorator : functions take another function/code as input, add or modify its behaivor,or add metadata,


# manual decorator structure 
# original function
# def hello():
#     print('hello')
    
# def my_decorator(original_func):
#     def wrapper():
#         print('before')
#         original_func()
#         print('after')
#         return wrapper
    
    
#     hello()
    
#     decoreted = my_decorator(hello)
#     decoreted()
    
#     # python shortcut syntax 
#     # @
#     @my_decorator
#     def say_hello():
#         print('hello')
        
        
#     say_hello()        
    

# import time
    

    
    
#     # Timing Decorator
    
# def timer_decorator(fun):
#     def wrapper():
#             start = time.time()
#             fun()
#             end = time.time()
#             print("time is : ", end -  start)
#     return wrapper
      
# @timer_decorator       
# def slow_func():
#         time.sleep(2)
#         print("finished")
        
        
# slow_func() 
# ========================================================

# return multiple values

# def numbers_():
#     num1 = 100
#     num2 = 500
#     num3 = 1000
#     return num1,num2,num3  # tuples (immutable array)
# print(numbers_())

# unpacking tuple --> destrucuting 

# a, b ,c = numbers_()

# print(a)
# print(b)
# print(c)

# lambda (anonymous function)

# regular function
# def square_ff(x,n):
#     return x**n 

# square_var = lambda x,n:x**n
# print(square_var(5,5))

 # =============================================================
 # type hints readable 

# age1: int = 33

# def add_fun(x: int, y:int) -> int:
#     return x+y

# print(add_fun(5,7))

 # documentation
# def good_night():
#     """
#     this function that the user uses to print goodnght
#     """
#     print('good night')
    
# print(good_night.__doc__)
    
     # ===========================================================
     # data strucure in python and built-in functions that we can use it here 
    
     # String (str) : ordered  , zero-based indexing , immutable sequence of characters
# string_1 = "hello Data engineering"
     # index = order - 1
    # space indexed as characters
# print(string_1[0]) 
# print(string_1[-1]) 


# #slicing 
# print(string_1[:6])
 # step by defualt 1 

# print(string_1[::2])

 # revese string

# print(string_1[::-1])

 # built in functions / methods
 # len(sequence) ==> return length (spaces included)

# print(len(string_1))

# .count("characters")  case sensitive
# print(string_1.count('l'))

# # .capitalize()

# print(string_1.capitalize())
 # upper()
# print(string_1.upper())

# # replace
# print(string_1.replace('e','@'))

# string_2= "             ABC     "

# # .leftstrip()

# print(string_2.lstrip())
# print(string_2.rstrip())
# print(string_2.strip())


# string_3 = "a b c d e"
 # split("seprator")  return array/list

# print(string_3.split(" "))
 # .find("characters")
 # index of first occurance if not found return -1
# print(string_1.find("h"))
# # concatenate
# print("mina","df")

# interpolation
# str_1 = 'mina '
# str_2 = 'data engineer'
# print(str_1 * 2 + str_2)

# # special character \n \t \\ \"  \' \r \b

# # formatted string 
# ms = 'hassan'
# # f-string
# print(f"hello {ms}")

# # fromat(var1,var2)
# message = "he is {0}, and he graduated from {1}"
# print(message.format('mina','is'))

# # .isalpha() = > false / true

# m1='mian'
# print(m1.isalpha())

# # isdigit()

# md2 = "565"
# print(md2.isdigit())
# print(md2.isnumeric())

# # .uppercase => .isupper() chick all the content of vars if they are upper case
# print(md2.islower())
# print(md2.isupper())

# # ==============================================================================
# # numbers (int , float , complex)
# a,v,b,d,g = 100,878,8779,41,4887
# # min(vars)
# print(min(a,v,g,b,d))

# print(max(a,v,g,b,d))
# # max(vars)

# # round 4 + 8j
# # lists [_, _, _ ],zero-based indexing ,mutable m elements from different types

# item = ["milk","egg","fruits","veg"]
# print(item)
# item[0] = "miklying"
# print(item)
# # casting any tyoe to list
# print(list(range(5)))
# # built in methods (mutating - non-mutating)

# numbers_list= [1,2,3,4,5,545,45,6]
# # sort() ==> mutating method 
# print(numbers_list)
# print(numbers_list.sort())
# print(numbers_list)
# print(numbers_list.sort(reverse=True))
# print(numbers_list)

# alpha = ["a","l","h","p","d","w","q",'545']
# print(alpha)
# print(alpha.sort())
# print(alpha)

# # reverse() ==> mutating method 
# alpha = ["a","l","h","p","d","w","q",'545']
# print(alpha.reverse())
# print(alpha)

# # .remove() ==> mutating method 
# print(numbers_list)
# print(numbers_list.remove(45))
# print(numbers_list)

# .pop() 
# print(numbers_list)
# print(numbers_list.pop(5))

# append()
# print(item)
# print(item.append('egg'))
# print(item)

# insert()
# print(item)
# print(item.insert(0,'egg'))
# print(item)

# item2 = ["rice","bananas"]
 # .extend(list) for adding lists 

# item.extend(item2)
# print(item)

# # list concatenation ==> non mutating method

# print(numbers_list + item)
# print(numbers_list)
# print(item)
# print(len(numbers_list)) #number of length
# last item index = len(sequence) - 1

# search for membership ==> case-sensitive
# print('egg' in item) 

# # max()
# print(max(numbers_list))

# looping over lists 
# for i in item:
#     print(i)
    # looping over index,items in the same list
    
# print(enumerate(item))


# for index,item in enumerate(item):
#     print(f"{index} -> {item}")
    
    
# names = ["veronia","ali","eman",'omnia']
# ages = [20,15,24,25]

# looping over two lists 

# 
# print(zip(names,ages)) 

# for i , j in zip(names,ages):
#     print(f"name : {i} , age : {j}")
    
# ============================================

# tuples {} ordered zero-indexed --- immutable

# t = (5,6,7)
# print(t)
# print((t[0]))

# t[0] = 23

# t1=tuple(numbers_list)
# print(t1)
#len(sequence)

# tuple from element (ended with ,)
# tup1 = ("apple",)
# for i in t : 
#     print(i)

# # set {_,_, _,_} unordered there is no index , mutable -- unique elements,no duplication

# s = {1,2,2,4,5,6,7,8,9,7,8,4}
# print(s)
# print(list(s))
# print(set(s))

# s.add(10)
# print(s)

# s.remove(10)
# print(s) #set()

# s.clear(5)
# print(s)


# union(set) ==> non-mutating method 

# s1 = {20,30}
# s2 = {16,13,20}


# new_set = s1.union(s2)
# print(new_set)

 # .difference (set)
# unique_set= s1.difference(s2)
# print(unique_set)



# intersection
# repeated_set= s1.intersection(s2)
# print(repeated_set)



# print(s1 | s2)  #union 
# print(s1 & s2)  # difference
# print(s1 - s2)  # intersection
# print(s1 ^ s2)  # symmetric difference


# dictionary : {"Key":"value","Key":"value","Key":"value","Key":"value","Key":"value"}   key-value pairs - key(index) is immutable and unique

# dict1 = {
    
#     "Key1":"value4",
#     "Key2":"value3",
#     "Key3":"value2",
#     "Key4":"value1",
# }

# print(dict1)

# # .get (key)

# print(dict1.get("Key1"))

# # .pop (key)

# print(dict1.pop("Key1"))
# print(dict1)

# dict1["Key2"] = 46

# print(dict1)

# .update (key)

# print(dict1.update("Key3"))
# print(dict1)


# key() ==> dict_keys(['m','d','ww'])

# values()
# print(dict1.values())
# print(list(dict1.values()))

# # membership

# print("hassan" in dict1)

# looping 
# python 3.6 ==> dictionaries is unordered
# python 3.7 ++ 


# iterate over values :
# for i in dict1.values():
#     print(i)

# # iterate over items
# for i in dict1.items():
#     print(i)