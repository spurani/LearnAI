"""
how to modify a global var inside a function
Ans: Then you have to put a global <var_name> inside the function
otherwise it would create a local var instead.

"""
a = 12  # global

def func():
    global a
    a = 200
    print(a)  #1

# global var can be used anywhere in the file

func()
print(a)  #2

