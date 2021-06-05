class CustomerNotAllowedException(Exception):
    pass
import re
from Customer import Customer

def CreateCustomer(customerdata):
    regex = re.compile('\s(?P<Pre>[^,\d]+),\s(?P<Post>.[a-zA-Z]*.)\s(?P<preost>[^,]+)\s,(?P<Pred>\d)')
    #for i in data:
        #print(i)
        #regex = re.compile('\s(?P<Pre>[^,\d]+),\s(?P<Post>.[a-zA-Z]*.)\s(?P<preost>[^,]+)\s,(?P<Pred>\d)')
    new_line = regex.findall(customerdata)[0]
    #print(new_line)
    title = new_line[1]
    firstname = new_line[2]
    lastname = new_line[0]
    blacklist = new_line[3]
    customer = Customer()
    customer.setFname(firstname)
    customer.setTitle(title)
    customer.setLname(lastname)
    customer.setIsblacklisted(blacklist)
    #print(customer.isblacklisted)
    return customer

def CreateOrder(customer,product):
    if(customer.isblacklisted == "1"):
        raise CustomerNotAllowedException
    else:
        print("Order Created for", customer)

data = open("651_m3_datasets_v1.0/FairDealCustomerData.csv",'r')
title = []
firstname = []
lastname = []
blacklist = []
list_of_cust = []
for i in data:
    list_of_cust.append(CreateCustomer(i.rstrip('\n')))
print(list_of_cust)
for i in range(0,2):
    try:
        CreateOrder(list_of_cust[i],"LCD")
    except CustomerNotAllowedException:
        print("Not Allowed")