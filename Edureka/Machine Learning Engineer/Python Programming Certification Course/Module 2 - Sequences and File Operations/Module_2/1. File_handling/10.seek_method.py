# .tell() method tells the position of file pointer

fo = open('bye.txt', 'r')
fo.seek(3,0)  # moves the file pointer by three positions from the beginning
print(fo.read())

fo.seek(0)
print("--- Going to read the content from beginning--")
print(fo.read())
fo.close()