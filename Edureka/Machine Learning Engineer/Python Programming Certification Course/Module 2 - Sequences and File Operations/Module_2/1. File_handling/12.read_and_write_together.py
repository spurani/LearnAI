"""
r+ allows both read and write but the file has to be present
w+ allows both read and write and if file is not present the it would be created
"""

fo = open('bye.txt', 'r+')
fo.write("Data science")
print("File pointer is at position %s"%fo.tell())
fo.seek(0)  # this brings the pointer back to origin
print(fo.read())  # now this will show the content
fo.close()