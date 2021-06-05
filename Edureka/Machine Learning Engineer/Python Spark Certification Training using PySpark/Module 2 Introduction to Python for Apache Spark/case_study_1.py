# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 20:41:57 2020

@author: SP
"""

'''
14.Write  a  program  to  compute  1/2+2/3+3/4+...+n/n+1 with a given  
n  input  by console (n>0).
Example:
If the following n is given as input to the program:5
Then, the output of the program should be:3.55
'''
# num = int(input("Please enter a number: "))
# final = 0
# for i in range(1,num+1):
#     final += i / (i + 1)
# print("%.2f" % final)

'''
13.Please write a program to randomly generate a list with 5 numbers,
which  are divisible by 5 and 7 , between 1 and 1000 inclusive.
'''
#lofn = [i for i in range(1,1001) if (i % 5 == 0)  if (i % 7 == 0)]
#print(lofn)
    
'''
12.By using list comprehension, please write a program to print the list 
after removing delete numbers which are divisible by 5 and 7 in 
[12,24,35,70,88,120,155].
'''
# l = [12,24,35,70,88,120,155]
# lofn = [i for i in l if(i % 5 != 0) if(i % 7 != 0)]
# print(lofn)

'''
11.By using list comprehension, please write a program to print the list 
after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155]
'''
# l = [12,24,35,70,88,120,155]
# lofn = [l[i] for i in range(len(l)) if(i!=0) if(i!=4) if(i!=5)]
# print(lofn)

'''
10.By using list comprehension, please write a program to 
print the list after removing the value 24 in [12,24,35,24,88,120,155].
'''
# l = [12,24,35,70,88,120,155]
# lofn = [i for i in l if(i != 24)]
# print(lofn)

'''
9.With a given list [12,24,35,24,88,120,155,88,120,155], 
write a program to print this list after removing all duplicate values 
with original order reserved.
'''
# l = [12,24,35,24,88,120,155,88,120,155]
# f = []
# for i in l:
#     if (i not in f):
#         f.append(i)

'''
8.With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], 
write a program to make a list whose elements are intersection of the 
above given lists.
'''
# a = [1,3,6,78,35,55]
# b = [12,24,35,24,88,120,155]
# lst3 = [value for value in a if value in b] 
# print(lst3)

'''
7.Please write a program which count and print the numbers of each 
character in a string input by console.Example: 
If the following string is given as input to the program:
abcdefgabc
Then, the output of the program should be:a,2c,2b,2e,1d,1g,1f,1
'''

# d = {}
# stringinput = input("PLease enter any alphabets: ")
# for i in stringinput:
#     if i in d: 
#         d[i] += 1
#     else: 
#         d[i] = 1
# print(str(d))

'''
6.Please write a program which accepts a string from console and 
print it in reverse order.Example: If the following string is given 
as input to the program: rise to vote sir
Then, the output of the program should be:ris etov ot esir
'''
# stringinput = input("PLease enter any alphabets: ")
# print(stringinput[::-1])
# print("".join(reversed(stringinput)))

'''
5.Please write a program which accepts a string from console and print 
the characters that have even indexes.Example: 
If the following string is given as input to the program:
H1e2l3l4o5w6o7r8l9d
Then, the output of the program should be:Helloworld
'''
# stringinput = input("Please enter: ")
# l = []
# for i in range(len(stringinput)):
#     if(i % 2 == 0):
#         l.append(stringinput[i])
# print("".join(l))

'''
4.Write a for loop that prints all elements of a list and their position 
in the list.a = [4,7,3,2,5,9] Hint: Use Loop to iterate through list 
elements.
'''
# a = [4,7,3,2,5,9]
# for i in range(len(a)):
#     print(a[i],"index: ",i)

'''
3.A website requires a user to input username and pas to register.
Write a program to check the validity of pas given by user. 
Following are the criteria for checking pas:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
3. At least 1 letter between [A-Z]
4. At least 1 character from [$#@]
5. Minimum length of transaction pas: 6
6. Maximum length of transaction pas: 12
Hint: In case ofinput data being supplied to the question, it should be assumed to be a console input.
'''
no_error = 0
e = 0
l = 0
n = 0
u = 0 
sc = 0
minl = 0
maxl = 0
final = 0
scl = ['$','#','@']
while final != 1:
    user = input("Please enter your username: ")
    pas = input("Please enter your pas: ")
    if(pas == ""):  
        print("1. At least 1 letter between [a-z]")
        print("2. At least 1 number between [0-9]")
        print("3. At least 1 letter between [A-Z]")
        print("4. At least 1 character from [$#@]")
        print("5. Minimum length of transaction pas: 6")
        print("6. Maximum length of transaction pas: 12")
    else:
        e = 1
        for i in pas:
            if(i.islower()):
                l += 1
            if(i.isupper()):
                u += 1
            if(i.isnumeric()):
                n += 1
            if(i in scl):
                sc += 1
        if((len(pas) >= 6) and (len(pas)) <= 12):
            minl = 1
            maxl = 1
        if(((e == 1) & (l >= 1) & (n >= 1) & (u >= 1) & (minl == 1) & (maxl == 1))):
            final = 1
        if(l == 0):
            print("At least 1 letter between [a-z]")
        if(n == 0):
            print("At least 1 number between [0-9]")
        if(u == 0):
            print("At least 1 letter between [A-Z]")
        if(sc == 0):
            print("At least 1 character from [$#@]")
        if(minl == 0):
            print("Minimum length of transaction pas: 6")
        if(maxl == 0):
            print("Maximum length of transaction pas: 12")