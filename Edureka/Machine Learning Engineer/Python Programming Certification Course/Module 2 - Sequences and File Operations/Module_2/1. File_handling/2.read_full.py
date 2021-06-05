# reading a full file in single shot

file_obj = open('bye.txt', 'r')

data = file_obj.read()
print(data)
file_obj.close()