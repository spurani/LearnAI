# # global and local
#
# a = 200  # global
#
# def func():
#     b = 100 # local
#
# print(b) # not accessible

a = 100   # global variable

def func():
    b = 200  # local variable
    print("Inside function Global var:%s"% a)
    print("Inside function local var:%s"% b)

func()
print("outside the function Global var:%s"% a)
print("Inside function local var:%s"%b)





















