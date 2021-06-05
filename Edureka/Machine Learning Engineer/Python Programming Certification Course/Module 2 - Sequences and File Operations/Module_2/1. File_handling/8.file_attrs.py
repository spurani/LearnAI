fo = open('bye.txt', 'w')

# 1 .closed attribute
print(fo.closed)
fo.close()
print(fo.closed)

# 2. mode
print(fo.mode)

# 3. name of the file
print(fo.name)



