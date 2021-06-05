# .tell() method tells the position of file pointer
# file pointer is a position from where next read or write would happen

fo = open('bye.txt', 'r')
print(fo.tell())
fo.read(2)
print(fo.tell())

fo.close()