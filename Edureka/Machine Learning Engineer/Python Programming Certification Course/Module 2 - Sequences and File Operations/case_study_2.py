# -*- coding: utf-8 -*-
"""
Module 2 Sequences and File Operators Case Study 2
"""
import base64
all_count = 0
special_chars = ["@","#","$"]
while all_count != 1: 
    print("Guide for reference id: ")
    print("Exactly 12 characters long including alphabets, numbers and anyone special character (@,#,$)")
    reference_id = input("Please enter reference id: ")
    count_d = 0
    count_sc = 0
    count_u = 0
    count_l = 0
    if(len(reference_id) == 12):
        for i in reference_id:
            if(i.isdigit()):
                count_d += 1
            if(i is not i.isdigit()):
                if(i in special_chars):
                    count_sc +=1
                if(i.isupper() == True):
                    count_u +=1
                if(i.islower() == True):
                    count_l += 1
        if(count_d < 5 or count_d > 5):
            print("Exactly 5 digits required")
        if(count_sc < 1 or count_sc > 1):
            print("Exactly 1 special character required")
        if(count_u < 1):
            print("Minimum 1 upper case character required")
        if(count_l < 1):
            print("Minimum 1 lower case character required")
        if(count_d == 5 and count_sc == 1 and count_u >= 1 and count_l >= 1): 
            en = reference_id.encode()
            encrypt_id = base64.encodebytes(en)
            print(encrypt_id)
            decrypt = input("Do you want to decrypt the reference id (Y/N): ")
            if(decrypt == "Y"):
                d = base64.decodebytes(encrypt_id)
                print(d)
                all_count = 1
            else:
                all_count = 1
    else:
        print("Length of your reference id should be exactly 12 characters long")
