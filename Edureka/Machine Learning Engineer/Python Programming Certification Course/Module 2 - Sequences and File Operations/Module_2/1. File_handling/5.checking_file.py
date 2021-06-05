import os

#1. check if the file exists
if os.path.exists('byee.txt'):
    print("yes file exists")
else:
    print("No it doesn't")


# # 2. check if the file is empty or not without opening it
# stat_info = os.stat('bye.txt')
# print(stat_info.st_size) # output is in bytes
# #I didn't get why we are getting extra line in the middle as space