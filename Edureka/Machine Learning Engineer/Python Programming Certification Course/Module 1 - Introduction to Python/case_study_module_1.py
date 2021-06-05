# -*- coding: utf-8 -*-
"""
Case Study Module 1–Introduction to Python
"""

''' 1. Write a program which will find factors of given number and find whether 
the factor is even or odd.Hint: Use Loop with if-else statements'''
c = 6
for i in range(1,c+1):
    if(6 % i == 0):
        print(i,"is factor of",c)
        if(i % 2 ==0):
            print(i," is even")
        else:
            print(i," is odd")
"""
2.Write a code which accepts a sequence of words as input and prints the words 
in a sequence after sorting them alphabetically. Hint: In case of 
input data being supplied to the question, it should be assumed to be a 
console input.
"""
words = input("Enter few words: ");
words = words.split()
words.sort()
for i in words:
    print(i)

"""
3.Write a program, which will find all the numbers between 1000 and 3000 (both included)
such that each digit of a number is an even number. The numbers obtained should be printed
in a comma separated sequence on a single line.Hint: In case of input data being supplied 
to the question, it should be assumed to be a console input.Divide each digit with 2 and 
verify is it even or not.
"""
a = []
for i in range(1000,3001):
    if(i % 2 == 0):
        a.append(i)
print(a)

"""
4.Write a program that accepts a sentence and calculate the number of letters and 
digits.Suppose if the entered string is: Python0325
Then the output will be:
    LETTERS: 6
    DIGITS:4
Hint: Use built-in functions of string.
"""
digits = 0;
letters = 0
letter_digits = input("Please enter string: ")
for i in letter_digits:
    if(i.isdigit()):
        digits += 1
    else:
        letters += 1

print("LETTERS: ",letters)
print("DIGITS: ",digits)

"""
5.Design a code which will find the given number is Palindrome number or not.
Hint: Use built-in functions of string.
"""
num = input("Enter any number to check if it is palindrome or not: ")
num1 = num[::-1]
if(num1 == num):
    print("Entered number ",num," is palindrome")
else:
    print("Entered number ",num," is not a palindrome")