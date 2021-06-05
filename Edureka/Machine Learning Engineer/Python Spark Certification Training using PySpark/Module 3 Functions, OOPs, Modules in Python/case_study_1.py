# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 20:33:09 2020

@author: SP
"""
import math

'''15) Give example of fsum and sum function of math library.'''
# print(math.fsum([1,2,3,4,5]))
# print(sum([1,2,3,4,5]))

'''14) Write a program that accepts a sentence and calculate the number of 
upper case letters and lower case  letters.Suppose the following input is 
supplied to the program:Hello world! Then, the output should be:
UPPER CASE 1LOWER CASE 9'''
# u_count = 0
# l_count = 0

# letters = input("Please enter the string: ")
# for i in letters:
#     if(i.isupper()):
#         u_count += 1
#     if(i.islower()):
#         l_count += 1
# print("Upper Case: ",u_count)
# print("Lower Case: ",l_count)

'''13.Write a program which accepts a sequence of comma separated 4 digit binary 
numbers as its input and then check whether they are divisible by 5 or not.
The numbers that are divisible by 5 are to be printed in a comma separated 
sequence.
0100,0011,1010,1001Then the output should be:1010
'''
# numbers = input("Please enter the 4 digit number separated by comma: ")
# l = numbers.split(',')
# for i in l:
#     if(int(i) % 5 == 0):
#         print(i)

'''
12.Write a program that accepts a sequence of whitespace separated words as 
input and prints the words after removing all duplicate words and sorting 
them alphanumerically. Suppose the following input is supplied to the 
program:hello world and practice makes perfect and hello world again
Then, the output should be:again and hello makes perfect practice world
'''
# seq = input("Write a sequence of whitespace separated words: ")
# l = seq.split(" ")
# print(set(l))
# s = set(l)
# print(" ".join(sorted(s)))

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
#seq = input("Write a sequence of line: ")
#print(seq.upper())
'''
10.Write a program that accepts a comma separated sequence of words as input 
and prints the words in a comma-separated sequence after sorting them 
alphabetically. Suppose the following input is supplied to the program:without,hello,bag,worldThen, the output should be:bag,hello,without,world
'''
# seq = input("Please write comma separated sequence of words: ")
# ssplit = seq.split(",")
# print(",".join(sorted(ssplit)))

'''
9.Write a program which can compute the factorial of a given numbers. 
Use recursion to find it. Hint: Suppose the following input is supplied 
to the program:8Then, the output should be:40320
'''
# def recur_factorial(n):
#    if n == 1:
#        return n
#    else:
#        return n*recur_factorial(n-1)

# num = 8

# # check if the number is negative
# if num < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    print("The factorial of", num, "is", recur_factorial(num))
   
'''
8. Write a program which will find all such numbers which are divisible by 7 
but are not a multiple of 5, between 2000 and 3200 (both included). 
The numbers obtained should be printed in acomma-separated sequence on a 
single line.
'''
# l = [x for x in range(2000,3201) if((x % 5 != 0) and (x % 7 == 0)) ]
# print(l)

'''
7. Design a software for bank system. There should be options like cash 
withdraw, cash credit and change password. According to user input, 
the software should provide required output.Hint: Use if else statements 
and functions.
'''
# class Bank_Account: 
#     def __init__(self): 
#         self.balance=0
#         print("Hello!!! Welcome to the Deposit & Withdrawal Machine") 
  
#     def deposit(self): 
#         amount=float(input("Enter amount to be Deposited: ")) 
#         self.balance += amount 
#         print("\n Amount Deposited:",amount)
#         print("\n Balance:",self.balance)
  
#     def withdraw(self): 
#         amount = float(input("Enter amount to be Withdrawn: ")) 
#         if self.balance>=amount: 
#             self.balance-=amount 
#             print("\n You Withdraw:", amount)
#             print("\n Balance:",self.balance)
#         else: 
#             print("\n Insufficient balance  ") 
  
#     def display(self): 
#         print("\n Net Available Balance=",self.balance) 
  
# # Driver code 
   
# # creating an object of class 
# s = Bank_Account() 
   
# # Calling functions with that class object 
# s.deposit() 
# s.withdraw() 
# s.display() 
    
'''
6. Write a program which takes 2 digits, X,Y as input and generates a 
2-dimensional array. The element value in the i-th row and j-th column of 
the array should be i*j.Note: i=0,1.., X-1; j=0,1,¡-Y-1.
'''
# input_str = input("Enter dimensions of array")
# dimensions=[int(x) for x in input_str.split(',')]
# rowNum=dimensions[0]
# colNum=dimensions[1]
# multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
# print(multilist)
# for row in range(rowNum):
#   for col in range(colNum):
#       multilist[row][col]= row*col
# print(multilist)

'''
5. Write a program that calculates and prints the value according 
to the given formula:Q = Square root of [(2 * C * D)/H]Following are 
the fixed values of C and H: C is 50. H is 30.D  is  the  variable  whose 
values  should  be  input  to  your  program  in  a  comma-separated sequence.
'''
h = 30
c = 50
numbers = input("please enter comma separated numbers to calculate sqrt: ")
number = list(numbers.split(","))
print(number)
for d in number:
    print((math.sqrt(2 * c * int(d))) / h)