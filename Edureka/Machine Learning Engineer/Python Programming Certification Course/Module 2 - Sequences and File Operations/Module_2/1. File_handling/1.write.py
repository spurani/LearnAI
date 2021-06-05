# File-Handling

file_obj = open('bye.txt', 'w')

for elem in range(10):
    file_obj.write("Edureka rocks"+str(elem)+'\n')
file_obj.close()