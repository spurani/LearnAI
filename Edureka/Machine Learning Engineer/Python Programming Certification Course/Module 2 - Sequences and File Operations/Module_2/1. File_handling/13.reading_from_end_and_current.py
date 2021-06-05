# fo = open('bye.txt', 'rb')
# fo.seek(2 , 0)  # seek(2)
# print(fo.read(4))
# fo.seek(3, 1)
# print(fo.read())
# fo.close()
# reading from the end

fo = open('bye.txt', 'rb')

fo.seek(-8, 2)
print(fo.read())
fo.close()
