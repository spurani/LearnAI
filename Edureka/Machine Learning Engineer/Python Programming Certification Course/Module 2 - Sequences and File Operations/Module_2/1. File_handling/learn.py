

# context-managers
# automatically closing a file using 'with'

with open("bye.txt", 'r') as file_obj:
    print(file_obj.read())
    print(file_obj.closed)


print(file_obj.closed)
