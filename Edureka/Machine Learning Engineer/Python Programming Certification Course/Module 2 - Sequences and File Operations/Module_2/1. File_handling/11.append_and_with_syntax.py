# 'a' mode append the data to a file , so file pointer would be at the end of file

with open('bye.txt', 'a') as fo:
    print(fo.tell())
    fo.write("Python rocks")

# you don't have to call close() method explicitly here with context manager
