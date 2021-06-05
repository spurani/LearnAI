# reading a full file in line by line

file_obj = open('bye.txt', 'r')

for line_data in file_obj:
    print(line_data)
file_obj.close()

# edureka rocks 1 is also after /n
# but there is no line space before bye but there is a line space before edureka rocks 1
