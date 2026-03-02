# ===========================================
# Write a program that counts up the number of vowels a, e, i, o, u contained in the string.
# ===========================================
text =input('Please put your phrases:  ').lower()

vowles = ['a','e','i','o','u']
count = 0
for i in text :
    if i in vowles: 
        count +=1
        
print('Number of vowles :',count)
# ===========================================
# Write a program that prints the number of times the string 'iti' occurs in any string.
# ===========================================
text =input('Please put your phrases:  ').lower()

count = text.count("iti")   
print('Number of iti :',count)
# ===========================================
# Write a program that remove all vowels from the input word and generate a brief version of it.
# ===========================================
text =input('Please put your phrases:  ')
vowles = 'aioueAEOIU'
new_text = ''

for i in text :
    if i not in vowles:
        new_text+= i
        
print("biref text is  : ",new_text)

# ===========================================
# Write a program that prints the locations of "i" character in any string you added
# ===========================================
text =input('Please put your phrases:  ')
target_i = 'i'
for index,char in enumerate(text):
    if char ==target_i:
        print(index, end=' ')

# ===========================================
# Ask the user for his name then confirm that he has entered his name (not an emptystring/integers).
# then proceed to ask him for his email and print all this data then
# check if it is a valid email or not ( valid email has @ and . )
# ===========================================

while True:
    name = input('Enter your Name :  ')
    if name.isalpha():
        break
    else:
        print('please Enter a valid name !!')
    
email = input('Enter your email : ')

print('\nUser Data :')
print('name :',name)
print('email : ',email)


if '@' in email and '.' in email:
    print('the email is valid.')
else:
    print('the email is unvalid !!!!!')
    
# ===========================================

#Given a string, s = "The quick brown fox jumps over the lazy
# dog", perform the following operations:
# ▪ Convert the entire string to uppercase.
# ▪ Find the position of the substring "fox".
# ▪ Count the number of occurrences of the letter "o".
# ▪ Replace the word "lazy" with "active".
# ▪ Split the string into a list of words.
# o Print the results of each operation.

# ===========================================
s = "The quick brown fox jumps over the lazy dog"
# ===========================================

print("Convert the entire string to uppercase :\n",s.upper())

# ===========================================
word = 'fox'
index = s.find(word)
if index != -1:
    print("the place of 'fox' is :",index)
else:
    print("the place of 'fox' is not found :")
# ============================================
count_o = 'o'
print(s.count(count_o))
# ============================================
replace_phrase = 'active'
print_ = s.replace('lazy','active')
print(print_)
# ============================================
split = s.split()
print(split)

# Given a string, s = "Data Science and Machine Learning", perform
# the following operations:
# ▪ Check if the string starts with "Data".
# ▪ Check if the string ends with "Learning".
# ▪ Check if all characters in the string are alphabetic.
# ▪ Find the first occurrence of the substring "and".
# ▪ Print the string in reverse order.
# o Print the results of each operation.

s = "Data Science and Machine Learning"

word = 'Data'
index = s.find(word)
if index != 0:
    print('not in the first place !!')
else:
    print('the word "Data" at the first place.')

# ============================================

word = 'Learning'
index = s.split()
if index[-1] == word:
    print('the word "Learning" at the last place.')

else:
    print('not in the last place !!')
    
# ============================================

print(s.replace(' ','').isalpha())

# ============================================

index = s.find('and')
print('the first occurance of "and" is : ',index)

# ============================================

reversed_s = s[::-1]
print("Reversed sting : " ,reversed_s)

# ============================================

# String Formatting
# o Given the following variables: name = "John", age = 25, and city =
# "New York", format a string that reads "John, aged 25, lives in New
# York".
# o Convert the formatted string to title case.
# o Center the formatted string in a 40-character wide string, padded with
# asterisks (*).
# o Print the results of each operation.

# ============================================
names = ["john"]
ages = [25]
city = ["New York"]

for i , j , m in zip(names,ages,city):
    print(f"name : {i} , age : {j} , city : {m}")
    
# ============================================

for i , j , m in zip(names,ages,city):
    print(f"name : {i.title()} , city : {m.title()}")
    
# ============================================

for i, j, m in zip(names, ages, city):
    formatted = f"name : {i.title()}, age : {j}, city : {m.title()}"
    centered = formatted.center(40, "*") 
    print(centered)

# ============================================
# Given a list, lst = [4, 2, 9, 1, 5, 6], perform the following
# operations:
# ▪ Append the number 7 to the list.
# ▪ Remove the number 2 from the list.
# ▪ Sort the list in ascending order.
# ▪ Reverse the order of the list.
# ▪ Find the index of the number 9.
# o Print the results of each operation.

lst = [4, 2, 9, 1, 5, 6]
# ============================================

lst_append = lst.append(7)
print(lst)

# ============================================

lst_remove = lst.remove(2)
print(lst)

# ============================================

lst_order = lst.sort()
print(lst)

# ============================================

lst_order = lst.sort(reverse=True)
print(lst)

# ============================================

lst_find = lst.index(9)
print(lst_find)

# ============================================
# Given a list, lst = [10, 20, 30, 40, 50, 60, 70, 80, 90], perform
# the following operations:
# ▪ Extract the sublist [30, 40, 50].
# ▪ Extract every second element from the list.
# ▪ Find the maximum and minimum values in the list.
# ▪ Replace the last element with 100.
# ▪ Print the list in reverse order.
# o Print the results of each operation.

# ============================================
lst = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# ============================================

extract = lst[2:5]
print(extract)
# ============================================
second = lst[1]
print(second)
# ============================================
min = min(lst)
max = max(lst)
print(min," : is the min value , ",max," : is the max value")
# ============================================
reversed_order = lst.sort(reverse=True)
print(lst)
# ============================================

# Given a tuple, tpl = (5, 10, 15, 20, 25, 30), perform the following
# operations:
# ▪ Find the index of the number 20.
# ▪ Count the number of times 15 appears in the tuple.
# ▪ Convert the tuple to a list and append the number 35.
# ▪ Convert the modified list back to a tuple.
# ▪ Print the length of the tuple.
# o Print the results of each operation.

# ============================================
tpl = (5, 10, 15, 20, 25, 30)

# ============================================
print(tpl.index(20))
# ============================================
count = 0

for i in tpl:
    if i == 15:
        count+=1
   
print("The number 15 appears", count, "time(s)")
# ============================================
tpl_to_list = list(tpl)
tpl_to_list.append(35)
print(tpl_to_list)
# ============================================
list_to_tuple = tuple(tpl_to_list)
print(list_to_tuple)
# ============================================
print(len(list_to_tuple))
# ============================================

# Given a tuple of strings, tpl = ("red", "blue", "green",
# "yellow"), perform the following operations:
# ▪ Check if "blue" is in the tuple.
# ▪ Find the index of "green".
# ▪ Slice the tuple to get the sub-tuple ("blue", "green").
# ▪ Concatenate the tuple with another tuple ("orange", "purple").
# ▪ Convert the tuple to a comma-separated string.
# o Print the results of each operation.
# ============================================
tpl = ("red", "blue", "green","yellow")
# ============================================

if 'blue' in tpl:
    print('blue is in the tuple.')
else:
    print('blue is in not the tuple !!!')
# ============================================
print(tpl.index('green'))
# ============================================
sub_tuple = tpl[1:3]
print(sub_tuple)
# ============================================
more_colors = ("orange", "purple")
all_colors = tpl + more_colors
print(all_colors)
# ============================================
print(",".join(tpl))

# ============================================
# Given a nested tuple, tpl = ((1, 2, 3), (4, 5, 6), (7, 8, 9)),
# perform the following operations:
# ▪ Access the element 5.
# ▪ Print the second tuple.
# ▪ Find the length of the first tuple.
# ▪ Convert the nested tuple into a flat list [1, 2, 3, 4, 5, 6, 7,
# 8, 9].
# ▪ Print the nested tuple in reverse order.
# o Print the results of each operation.
# ============================================

tpl = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
# ============================================
print(tpl[1][1])
# ============================================
print(tpl[1])
# ============================================
print(len(tpl[0]))
# ============================================
to_list = []
for i in tpl:
    for j in i:
        to_list.append(j)
        
print(to_list)
# ============================================
to_list = list(tpl)
desc = to_list.sort(reverse=True)
print(to_list)
