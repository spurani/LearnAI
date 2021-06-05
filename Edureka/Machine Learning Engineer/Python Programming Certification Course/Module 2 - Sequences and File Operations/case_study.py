# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 18:40:36 2020

@author: SP

Case Study - Module 2 - Sequence and File Operations
"""

"""
1.What is the output of the following code?
nums =set([1,1,2,3,3,3,4,4])
print(len(nums))
Hint:Set consists unique element.
"""
# nums = set([1,1,2,3,3,3,4,4])
# print(len(nums))

"""
2.What will be the output?
d ={"john":40, "peter":45}
print(list(d.keys()))
Hint:d.keys() is the function which will showkeys.
"""

# d={"john":40,"peter":45}
# print(list(d.keys()))

"""
3.A website requires a user to input username and password to register. 
Write a program to check the validity of password given by user. 
Following are the criteria for checking password:
    1. At least 1 letter between [a-z]
    2. At least 1 number between [0-9]
    3. At least 1 letter between [A-Z]
    4. At least 1 character from [$#@]
    5. Minimum length of transaction password: 6
    6. Maximum length of transaction password: 12
Hint: In case of input data being supplied to the question, 
it should be assumed to be a console input.
"""

special_character = ['$','#','@']
flag_all = 0
while flag_all != 1:
    flag_low = 0
    flag_up = 0
    flag_num = 0
    flag_sc = 0
    word = input("Enter password: ")
    if(len(word)>=6 or len(word)==12): 
        for i in word:
                if(i.islower()):
                    flag_low = 1
                if(i.isdigit()):
                    flag_num = 1
                if(i.isupper()):
                    flag_up = 1
                if(i in special_character):
                    flag_sc = 1
        if(flag_low == 0):
            print("At least 1 letter between [a-z]")
        if(flag_num == 0):
            print("At least 1 number between [0-9]")
        if(flag_up == 0):
            print("At least 1 letter between [A-Z]")
        if(flag_sc == 0):
            print("At least 1 character from [$#@]")
        if((flag_low == 1 and flag_num == 1 and flag_up == 1 and flag_sc == 1)):
            flag_all = 1
        if(flag_low == 0 and flag_num == 0 and flag_up == 0 and flag_sc == 0):
            flag_all = 0
    else:
        print("Minimum password length is 6 and Maximum pass word length is 12")

"""
4.Write a for loop that prints all elements of a list and their position in the list.
a = [4,7,3,2,5,9] 
Hint: Use Loop to iterate through list elements.
"""

#This is normal way
# a = [4,7,3,2,5,9]
# for i in range(len(a)):
#     print(i," ",a[i])
    
#using enumerate
# for i in enumerate(a):
#     print(a)

"""
5.Please write a program which accepts a string from console and print the characters
that have even indexes.Example: If the following string is given as input to the 
program:
H1e2l3l4o5w6o7r8l9d 
Then, the output of the program should be:Helloworld
"""

# string_index = input("Please enter string with indexes: ")
# final_string = ""
# for i in range(len(string_index)):
#     if(i % 2 == 0):
#         final_string += string_index[i]
# print(final_string)

"""
6.Please write a program which accepts a string from console and print it in reverse
order.Example: If the following string is given as input to the program: 
rise to vote sir Then, the output of the program should be:
ris etov ot esir
"""

#Using reversed()        
# r = ""
# reverse_order = input("Please enter string to reverse: ")
# for i in reversed(reverse_order):
#     r += i
# print(r)

#Using slicing/splicing don't recall the actual naming convention for this method
# print(reverse_order[::-1])

"""
7.Please write a program which count and print the numbers of each character in a 
string input by console.Example: If the following string is given as input to the
program:abcdefgabc  
Then, the output of the program should be:
a,2
c,2
b,2
e,1
d,1
g,1
f,1
"""

# final = {}
# char_count = input("Please enter a string: ")
# for i in range(len(char_count)):
#       for j in range(i+1,len(char_count)):
#               if(char_count[i]==char_count[j]):
#                   print(i,"i",char_count[i],"j=>",j,"char",char_count[j])
#                   if(char_count[i] not in final): 
#                       final.setdefault(char_count[i],1) 
#                       print(char_count[i],final[char_count[i]])
#                   else:
#                       final[char_count[i]] += 1
#                       print(i,"i",char_count[i],"j=>",j,"char",char_count[j],"else 1")
#               else:
#                   print(i,"i","j=>",j,"char",char_count[i])
#                   if(char_count[i] not in final): 
#                       final.setdefault(char_count[i],1)
#                       print(i,"i",char_count[i],"j=>",j,"char",char_count[j],"if else 1")
# print(final)

# dic = {}
# s=input('Enter string: ')
# for s in s:
#     dic[s] = dic.get(s,0)+1
# print('\n'.join(['%s,%s' % (k, v) for k, v in dic.items()]))
"""
8.With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write
a program to make a list whose elements are intersection of the above given lists.
"""

# a = [1,3,6,78,35,55]
# b = [12,24,35,24,88,120,155]

# c = set(a) & set(b)
# d = set(a).intersection(b)
# print(c)
# print(d)

"""
9.With a given list [12,24,35,24,88,120,155,88,120,155], 
write a program to print this list after removing all duplicate values with original 
order reserved.
"""
# final = []
# a = [12,24,35,24,88,120,155,88,120,155]
#a.reverse()
#print(a)
#reverse_l = list(reversed(a))
#print(reverse_l)

## second method pretty staright forward
# final = []
# without_duplicates = []
# for element in a:
#    if element not in without_duplicates:
#        without_duplicates.append(element)

# reverse_without_dup = reversed(without_duplicates)
# for i in reverse_without_dup:
#     final.append(i)
# print(final)

#third
# def removeDuplicate( li ):
#     newli=[]
#     seen = set()
#     for item in li:
#         if item not in seen:
#             seen.add( item )
#             newli.append(item)
#     return newli

# new_list = removeDuplicate(a)
# print(new_list[::-1])

"""
10.By using list comprehension, please write a program to print the list after 
removing the value 24 in [12,24,35,24,88,120,155].
"""
# wel = [12,24,35,24,88,120,155]
# print([x for x in wel if x!=24])

"""
11.By using list comprehension, please write a program to print the list after 
removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].
"""
#eleven = [12,24,35,70,88,120,155]
#print([eleven[x] for x in range(len(eleven)) if(x != 0 and x != 4 and x != 5)])

"""
12.By using list comprehension, please write a program to print the list after 
removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
"""

# twelve = [12,24,35,70,88,120,155]
# print([x for x in twelve if(x % 5 != 0 and x % 7 != 0 )])

"""
13.Please write a program to randomly generate a list with 5 numbers, which are 
divisible by 5 and 7 , between 1 and 1000 inclusive.
"""
# import random
# print(random.sample([i for i in range(1,1001) if i%5==0 and i%7==0], 5))

"""
14.Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console 
(n>0).Example:If the following n is given as input to the program:5
Then, the output of the program should be:3.55
"""
# ans = 0
# num = int(input("Enter a number: "))
# for x in range(1,num+1):
#     ans += round(x/(x+1),2)
# print(ans)
