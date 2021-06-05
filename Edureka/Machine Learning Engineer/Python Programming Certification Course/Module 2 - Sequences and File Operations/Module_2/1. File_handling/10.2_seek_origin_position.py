"""
seek(<characters_to_jump>, <from_where>): moves the position of file-cursor
<from_where> can take 3 values
0: means jump from the origin i.e 0 position
1: means jump from the current file cursor position in the file
2 : means jump from the end of the file.
 NOTE: make sure you use binary mode for 1 and 2.
"""

# case: moving the file cursor to origin/initial file position
# <from_where> = 0

file_obj = open('bye.txt', 'rb')
print(file_obj.tell())
file_obj.read(3)
print(file_obj.tell())

file_obj.seek(2, 0)
#
print(file_obj.read())
file_obj.close()

# PEP 8: coding guidelines

