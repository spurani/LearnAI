# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 15:41:39 2020

@author: SP
"""
import requests
from bs4 import BeautifulSoup

# enter = input("Please enter url to fetch hyperlinks: ")
# r = requests.get(enter)
# c = r.content
# soup = BeautifulSoup(c,"html.parser")
# for link in soup.find_all('a'):
#     print(link.get('href'))

r = open("s.html","r")
rd = r.read()
links = []
soup = BeautifulSoup(rd,"html.parser")
#print(soup.prettify())
# for link in soup.find_all('a'):
#         print(link.get('href'))
# for link in soup.find_all('b'):
#     print(link.text)
# for link in soup.find_all('b'):
#         print(link)
# for link in soup.find_all():
#         print(link)
# for link in soup.find_all():
#     if(len(link.attrs) == 2):
#         print(link)
# for link in soup.find_all():
#     if((len(link.attrs) == 0) & (len(link.name) == 1) ):
#         print(link)

#for link in soup.find_all():
    # if(link['align'] == 'center'):
#        print(link.attrs)
xml = """<person name="Bob">
         <parent rel="mother" name="Alice">
"""
ff = BeautifulSoup(xml,'xml')
for j in ff.find_all(attrs={'name':'Alice'}):
     print(j)

