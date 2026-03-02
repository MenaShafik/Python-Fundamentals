# ----------------------------------------------------------------------------------------------
    
    # Write a program that prints the following output using one single print() statement only:
    # Python|IO|Lab
    # Done
# ----------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------
# Ask the user to enter three values, one at a time.
# For each value:
# •	Print the value itself
# •	Print its detected type after attempting conversion in this order:
# 1.	int
# 2.	float
# 3.	otherwise keep it as str
# Rules:
# •	No exceptions (try/except) allowed
# •	Use logical checks and casting behavior only
for i in range(1):
       x=int(input())
       y=float(input())
       z=input()
       print(x,y,z)
       print(type(x),type(y),type(z))
       
# ----------------------------------------------------------------------------------------------


item = [0, "0", "", [], [0], None]

for i in item:
    print("value:", bool(i))
# ----------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------

# Question 4 – Arithmetic Decision Engine
# Input two integers from the user.
# Perform all of the following operations:
# •	Addition
# •	Floor division
# •	Modulus
# •	Power
# Then:
# •	If any result equals zero, print "Zero Detected"
# •	Otherwise print "All Non-Zero"
input_1 = int(input("First_integer :"))
input_2 = int(input("First_integer :"))
print('addition is : ',input_1+input_2)