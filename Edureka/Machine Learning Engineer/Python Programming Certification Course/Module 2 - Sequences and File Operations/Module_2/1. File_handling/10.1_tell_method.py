# tell():  next read/write position in a file

file_obj = open('bingo.txt', 'r')
print("File pointer Initially",file_obj.tell())
file_obj.read(3)
print("File pointer after first read method",file_obj.tell())
print(file_obj.read())
print("File pointer after second read method",file_obj.tell())
file_obj.close()

