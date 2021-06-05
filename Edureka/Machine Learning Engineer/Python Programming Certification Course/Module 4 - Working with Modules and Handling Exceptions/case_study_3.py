# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 22:48:01 2020

@author: SP
"""
from Customer import Customer
import re

class CustomerNotAllowed(Exception):

    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def CreateCustomer(data):
    new_line = []
    customer_obj = Customer()
    regex = re.compile('\s(?P<Pre>[^,\d]+),\s(?P<Post>.[a-zA-Z]*.)\s(?P<preost>[^,]+)\s,(?P<Pred>\d)')
    new_line = regex.findall(data)[0]
    customer_obj.setTitle(new_line[1])
    customer_obj.setFname(new_line[0])    
    customer_obj.setLname(new_line[2])
    customer_obj.setIsblacklisted(new_line[3])
    return customer_obj

def createOrder(customer,product):
            if(customer.isblacklisted() == "1"): 
                raise CustomerNotAllowed("Customer is Black Listed:" + customer.__str__())
            else:
                print("Order created successfully for:" + customer.__str__())
                print()

            customer_list = []
            with open("FairDealCustomerData.csv") as file:
                for i in file:
                    customer_list.append(CreateCustomer(i))
            file.close()
            print ("No . of customers read from file:",len(customer_list))
            
            for i in range(0,2):
                try: 
                    createOrder(customer_list[i]," LEDTV")
                except CustomerNotAllowed as customexception:
                    print(" Exception Customer NotAllowed handled message", customexception)
                finally:
                    print ("End of Program")
        

