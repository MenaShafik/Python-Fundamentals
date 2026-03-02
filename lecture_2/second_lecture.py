# # # special characters  in strings :
# # # \"

# name = 'mina is not bad \n'
# skipping = 'and \"is" good\n'
# print(name+skipping)

# # # escaping backslash ==> \\
# msasn = 'im 20 \\years\\'
# print(msasn)

# # # calculations & operations!

# # # unary -- binary -- 
# # x=5
# # vaiable_name = +5
# # variable_num = -5

# # # binary operators 
# # variable_num + variable_num

# # # ternary operators 
# # age = 20
# # state  = 'adult' if age >= 18 else 'minor'
# # print(state)

# # # operations
# # # when we divide two int the result will be  a float 
# # # that we called ot implicit casting :
# # # item_1 = 11
# # # item_2 = 3
# # # res = item_1 / item_2
# # # print(res)
# # # power --- remainder ---
# # # comparsion operators < > == != bang

# # # x = 10 < 5
# # # print(x)


# # # x = 10 != 5
# # # print(x)

# # # logical operators : AND,OR,NOT


# # # truthy or falsy : 
# # print('--------------------- truthy and falsy ------------------------')
# # # truthy bool(value) => true
# # x= 10 
# # # true
# # y = '' 
# # # false
# # print(bool(y))

# # # sequence flow

# # # selection / conditional statements 

# # # if statment 
# # # condition must be in descending order
# # # temp = int(input("please enter the temp : "));
# # # if temp > 30 :
# # #                print('wither is hot')
# # # elif temp >20 :
# # #     print('the wiether is good')
# # # else : print('wither is cold ')
# # # match expression:
# # #     case pattern:
# # #     case pattern1:
# # #     case_:
# #         # defualt case 
# # # status_code = 404
# # # match status_code:
# # #     case 200:
# # #         print('ok')
# # #     case 404:
# # #         print('not found')
# # #     case 500:
# # #         print('server error')
# # #     case _:
# # #         print('unkown state')
                
# #             # ====================
# # # day = int(input('please enter the day of the week order'))
# # # match day:
# # #     case 1 | 2 | 3 | 4  | 5 :
# # #         print('weekdays')
# # #     case 6|7 :
# # #         print('weekend')
# # # looping 
# # # print(list(range(1,5,2)))

# # # 1 arg => stop excluded => start from 1 and stop at 5 and step is 2

# for i in range(1,6,2):
#     print(i)
    
# #     # in definite iteration
    
    
    
    
    
# #     #  else with loops 
# # # for i in range(5):
# # #         print(i)
# # # else:
# # #         print('else execited')
        
        
# #       def  # function_name()
# #         # no parameters , no return

# def great():
#     print('hello')
#     print('data enginerring')
            
            
# great()

# # # def geed_name(name):
# # #     print('hello,',name)
    
    
    
    
# # # geed_name('mina')


# # # def greed_with_return():
# # #     return 'hi,mina'


# # # print(greed_with_return()) <==  volatile 
# # # result = greed_with_return() ==> non volatile
# # # print(result)
# # # non_volatile <==

# # # def add(x,y):
# # #     result = x+y
# # #     return result

# # # add1 = add(45,65)
# # # print(add1)


# # # default patamrter
# # def greed_with_defualt(name="Guest"):
# #     print('hi,',name)
    
    
    
# # greed_with_defualt()
# # greed_with_defualt("abdalla")

# # # *ARGS

# # def total(*args):
# #     return sum(args)


# # print(total(1,2,5,4))



# # # strings concatenation

# # x= 'mina '
# # y= 'shafik'
# print(x+y)

# # def fullname(*args):
# #     fullname= ""
# #     for i in args:
# #         fullname+=i + " "
# #     return fullname
    
# # print(fullname("mina","shafik","reyad"))
    
    
    
    
    
    
    
    
# month = int(input("Enter a month number : "))

# match month:
#     case 1|2| 3:
#         print("Q1")
#     case 4|5|6 :
#         print("Q2")
#     case 7|8|9:
#         print("Q3")
#     case 10|11|12:
#         print("Q4")
#     case _:
#         print("Invalid")
# x=int(input())
# y=float(input())
# z=input()
# print(x,y,z)
# print(type(x),type(y),type(z))