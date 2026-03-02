# ==============================================
# Question 1 – Controlled Output Formatting
# print('Python ',' IO ',' Lab ',sep='|',end="\n")
# print("Done")

# ==============================================
# Question 2 – Dynamic Type Inspection

for i in range(1):
       x=int(input())
       y=float(input())
       z=input()
       print(x,y,z)
       print(type(x),type(y),type(z))
       

# ==============================================
# Question 3 – Truthy / Falsy Analyzer

item = [0, "0", "", [], [0], None]

for i in item:
    print("value:", bool(i))
    
# =======================================
# Question 4 – Arithmetic Decision Engine    


input_1 = int(input("First_integer :"))
input_2 = int(input("First_integer :"))
print('addition is : ',input_1+input_2)
print('Power is :', input_1 ** input_2)


if input_2 != 0:
    print('Floor division is : ', input_1 // input_2)
    print('Modulus is :', input_1 % input_2)
    print('non Zero Detected')
else:
    print('Zero Detected')


# =======================================
# Question 5 – Conditional Classification

user_value = int(input('Enter your age : '))
if user_value >=60:
    print('senior')
elif user_value >=18 & user_value <= 59:
    print('Adult')
elif user_value >=13 & user_value <=17:
    print('Teen')
elif user_value < 13:
    print('child')
else: 
    print('not found')
    
    # ==============================================
    # Question 6 – match Without Direct Values
    
    
month = int(input("Enter a month number : "))

match month:
    case 1|2| 3:
        print("Q1")
    case 4|5|6 :
        print("Q2")
    case 7|8|9:
        print("Q3")
    case 10|11|12:
        print("Q4")
    case _:
        print("Invalid")


    # ==============================================
    #Question 7 – Range Logic Validation
    
for i in range(2,21,2):
    print(i)
    
    # ==============================================
    # Question 8 – Password Simulation Loop
    
correct_password = "mina12"

attempts = 0
password = "" 

while password != correct_password:
    password = input("Enter password: ")
    attempts += 1

print(f"Access Granted After {attempts} Attempts")


# ==============================================
# Question 9 – Loop else Logic
arr = [2, 4, 6, 8, 10]
for i in arr:
    if i == 7:
        print('found')
        
    else:
        print('not found')
        
    
# ==============================================
# Question 10 – Function-Based Calculator

def calculate_average(*args):
    if len(args) == 0:
        return "Invalid"
    else:
        total = sum(args)
        count = len(args)
        return total / count

print(calculate_average()) 
print(calculate_average(10, 20))        
print(calculate_average(1, 2, 3, 4, 5)) 
