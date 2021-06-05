# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 21:22:30 2020

@author: SP
"""
import base64
n = 0
a = 0
import sys
print(sys.argv[1])
for i in sys.argv:
    if(len(i)<12):
        print("length is less than 12 please enter.")
    else:
        for alphanumeric in i:
            if(alphanumeric.isnumeric() != True):
                n += 1
            if(alphanumeric.isalpha() != True):
                a += 1
if(n == 0):
    print("It is not numeric atleast one numeric required")
if(a == 0):
    print("It is not alphabetic atleast one alphabet required")
if((n > 0) & (a > 0)):
    encoded = sys.argv[1].encode('ascii')
    base64_bytes = base64.b64encode(encoded)
    base64_message = base64_bytes.decode('ascii')
    print(base64_message)
    y = input("Please press y to decode the encoded ID: ")
    if(y == 'y'):
        decoded = base64_message.encode('ascii')
        message_bytes = base64.b64decode(decoded)
        message = message_bytes.decode('ascii')
        print(message)