# reading a full file in line by line using .readline() function

file_obj = open('bye.txt', 'r')

while True:
    line_data = file_obj.readline()
    if line_data: # if line_data is not empty then go inside the loop
        print(line_data)
    else:
        break

file_obj.close()
# How does the while loop 1: know how many lines we have in the file?