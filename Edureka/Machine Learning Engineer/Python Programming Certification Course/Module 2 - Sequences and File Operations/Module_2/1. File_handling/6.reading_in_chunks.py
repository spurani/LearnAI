# reading file in chunks

file_obj = open('bye.txt', 'r')

while 1:
    line_data = file_obj.read(5)
    if line_data:
        print(line_data)
    else:
        break

file_obj.close()



