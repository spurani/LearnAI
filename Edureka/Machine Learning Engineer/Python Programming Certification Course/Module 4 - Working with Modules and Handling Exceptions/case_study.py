# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 10:13:35 2020

@author: SP
"""
'''
1.A Robot moves in a Plane starting from the origin point (0,0).
The robot can move toward UP, DOWN, LEFT, RIGHT. 
The trace of Robot movement is as given following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after directions are steps.
Write a program to compute the distance current position after sequence of 
movements.
Hint: Use math module.
'''
'''import math
x,y = 0,0
while True:
    dir_step = input("Enter Direction with Step respectively: ")
    if not dir_step:
        break;
    dir_step = dir_step.split(" ")
    steps = int(dir_step[1])
    direction = dir_step[0]
    if(direction == "UP"):
        y += steps
    elif(direction == "DOWN"):
        y -= steps
    elif(direction == "LEFT"):
        x -= steps
    elif(direction == "RIGHT"):
        x += steps
distance = round(math.sqrt(x**2 + y**2))
print("Distance: ",distance)    
'''

'''
2.Data of XYZ company is stored in sorted list. 
Write a program for searching specific data from that list.
Hint: Use if/elif to deal with conditions.
'''    
# list = [2,5,9,8,1,3] 
# list_sorted= sorted(list)
# print(list_sorted)

# while True:
#     number = input("Enter a number to search in list and Press E to exit: ")
#     print(number)
#     if(number == "E"):
#         break
#     elif(int(number) in list):
#         print("Number is present in list")
#     elif(int(number) not in list_sorted):
#         print("Number is not present in list")

# import math
# def bin_search(li, element):
#  bottom = 0
#  top = len(li)-1
#  index = -1
#  while top>=bottom and index==-1:
#      mid = int(math.floor((top+bottom)/2.0))
#      if li[mid]==element:
#          index = mid
#      elif li[mid]>element:
#         top = mid-1
#      else:
#         bottom = mid+1
#      return(index)

# li=[1,11,23,34,45,56]
# print(bin_search(li,11))
# print(bin_search(li,12))

'''
3.Weather forecasting organization wants to show is it day or night.
So, write a program for such organization to find whether is it dark 
outside or not.Hint: Use time module.
'''
'''import time
print("Is it dark outside?\n==================")
#month_number : sunset_hour
dark = {
 1: 16,
 2: 17,
 3: 18,
 4: 19,
 5: 19,
 6: 20,
 7: 20,
 8: 19,
 9: 18,
 10: 17,
 11: 17,
 12: 16
 }
#month_number : sunrise_hour
light = {
 1: 8,
 2: 7,
 3: 6,
 4: 5,
 5: 4,
 6: 4,
 7: 4,
 8: 5,
 9: 6,
 10: 6,
 11: 7,
 12: 8
 }   
current_time = time.localtime()
print(current_time.tm_hour,current_time.tm_min,current_time.tm_sec,"Month: ",current_time.tm_mon)
if(current_time.tm_hour <= dark[current_time.tm_mon] or current_time.tm_hour >= light[current_time.tm_mon]):
    print("LIGHT")
if(current_time.tm_hour >= dark[current_time.tm_mon] or current_time.tm_hour <= light[current_time.tm_mon]):
    print("DARK")'''

'''
4.Write a program to find distance between two locations when their 
latitude and longitudes are given.Hint: Use math module.
'''

'''from math import sin, cos, sqrt, atan2, radians
# approximate radius of earth in km
R = 6373.0
lat1 = radians(52.2296756)
lon1 = radians(21.0122287)
lat2 = radians(52.406374)
lon2 = radians(16.9251681)
dlon = lon2 - lon1
dlat = lat2 - lat1
a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))
distance = R * c
print("Result:", distance)
print("Should be:", 278.546, "km")'''

'''
5.Design a software for bank system. There should be options like cash withdraw,
cash credit and change password. 
According to user input, the software should provide required output.
Hint: Use if else statements and functions.
'''
# amount = 0

def checkbalance(amount):
    return print("Your current account balance is: ",amount)

# def withdraw():
#     balance = checkbalance(amount) 
#     #amount = input("Please enter amount to withdraw: ")
#     if(value > balance):
#         return "Your account balance is not enough to proceed with transaction"
#     else:
#         if(balance != 0):
#             balance -= value
#             checkbalance(balance)
            
        
# def addbalance():
#     amount = int(input("Please enter amount to deposit: "))
#     if(amount < 0):
#         print("Invalid Amount")
#     else:
#         amount += amount
#     return amount

# while True:
#         option = int(input("Select any of the below options: "))
#         print("1) Withdraw cash")
#         print("2) Check balance")
#         print("3) Deposit balance")
#         print("4) Cash credit")
#         print("5) Change password") 

#         # if(option == 1):
#         #     withdraw()
#         if(option == 2):
#             checkbalance(amount)
#         if(option == 3):
#             addbalance()
#         # if(option == 4):
#         #     cashcredit()
#         # if(option == 5):
#         #     changepassword()
#         if(option == 0):
#             break

'''
6.Write a program which will find all such numbers which are divisible by 7 
but are not a multiple of 5, between 2000 and 3200 (both included). 
The numbers obtained should be printed in acomma-separated sequence on a 
single line.
'''
#print([i for i in range(2000,3201) if i % 7 == 0 and i % 5 != 0])

'''
7.Write a program which can compute the factorial of a given numbers.
Use recursion to find it. Hint: Suppose the following input is supplied 
to the program:
8
Then, the output should be:40320
'''
# temp = 1
# number = int(input("Please enter a any number: "))
# Using for loop
# for i in range(1,number+1):
#     temp *=i
# print(temp)

#Using recurrsion
# def fact(x):
#  if x == 0:
#      return 1
#  return x * fact(x - 1)
# x=int(input("Enter number whos factorial you want to find"))
# print(fact(x))

'''
8.Write a program that calculates and prints the value according to the 
given formula:Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H: C is 50. H is 30.D is the variable 
whose values should be input to your program in a comma-separated sequence. 
Example:Let us assume the following comma separated input sequence is given to 
the program:100,150,180 The output of the program should be:18,22,24
'''
# import math
# D = input("Please enter number: ")
# D = D.split(",")
# C = 50
# H = 30
# ans = []
# for i in D:
#     ans.append(str(round(math.sqrt((2 * C * int(i)) / H))))
# print(','.join(ans))

'''
9.Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional
array. The element value in the i-th row and j-th column of the array should be
i*j.Note: i=0,1.., X-1; j=0,1,i-Y-1.
'''
# input_str = input("Enter dimensions of array")
# dimensions=[int(x) for x in input_str.split(',')]
# rowNum=dimensions[0]
# colNum=dimensions[1]
# multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
# print(multilist)
# for row in range(rowNum):
#  for col in range(colNum):
#      multilist[row][col]= row*col
# print(multilist)

'''
10.Write a program that accepts a comma separated sequence of words as input and
prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
'''
#words = input("Please enter comma separated words: ")
# words = words.split(",")
# sorter = sorted(words)
# final = []
# for i in sorter: 
#     final.append(str(i))
# print(','.join(final))

#second method
# items=[x for x in input('Enter strings').split(',')]
# items.sort()
# print(','.join(items))

'''
11.Write a program that accepts sequence of lines as input and prints the lines
after making all characters in the sentence capitalized. 
Suppose the following inputis supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
'''

# lines = []
# while True:
#  s = input("Enter string")
#  if s:
#      lines.append(s.upper())
#  else:
#      break;
# for sentence in lines:
#  print(sentence)

'''
12.Write a program that accepts a sequence of whitespace separated words as 
input and prints the words after removing all duplicate words and sorting them 
alphanumerically. Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:again and hello makes perfect practice world
'''

# sentence = input("Enter a sentence: ")
# sentence = sentence.split(" ")
# sentence = sorted(set(sentence))
# print(" ".join(sentence))

'''
13.Write a program which accepts a sequence of comma separated 4 digit binary
numbers as its input and then check whether they are divisible by 5 or not.
The numbers that are divisible by 5 are to be printed in a comma separated
sequence.
Example:
0100,0011,1010,1001
Then the output should be:1010
'''
# value = []
# items=[x for x in input("Ener 4 binary numbers").split(',')]
# for p in items:
#  intper = int(p, 2)
#  if not intper%5:
#      value.append(p)
# print(','.join(value))

'''
14.Write a program that accepts a sentence and calculate the number of uppercase
letters and lower case letters.Suppose the following input is supplied to the
program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''
# count_u = 0
# count_l = 0
# sentence = input("Enter a sentence: ")
# for i in sentence:
#     if(i.isupper()):
#         count_u += 1
#     if(i.islower()):
#         count_l += 1
# print("UPPER CASE",count_u)
# print("LOWER CASE",count_l)

'''
15.Give example of fsum and sum function of math library.
'''
import math
print(fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]))
