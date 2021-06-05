"""
1. __init__ is a constructor(not exactly but closest to it)
2. self : object reference

'init' stands for initialisation i.e when you create an  object if you wish
to have some attributes defined with the value then you would use __init__
"""


class EdurekaStudent:
    def __init__(self, a, b, c):
        self.name = a
        self.age = b
        self.course = c

    def show_name(self):
        print(self.name)
        self.hello()

    def hello(self):
        print("hello")


###### creating instances/objects ######
# instantiation
ravi_object = EdurekaStudent("Ravi", 23, "Python")

# what happens internally
#ravi_object.__init__(ravi_object, "Ravi", 23, "Python")

# how to access an attribute or call a method, outside the class
# Ans:use object/instance
print(ravi_object.name)
print(ravi_object.course)

# calling a method , outside the class
ravi_object.show_name() # ravi_object.show_name(ravi_object)

print("*"*10)
#student 2
shyam_obj = EdurekaStudent("Shyam", 24, "Django")
# internally
#shyam_obj.__init__(shyam_obj, "Shyam", 24, "Django")

print(shyam_obj.name)
print(shyam_obj.course)
shyam_obj.show_name()


# # is self a keyword ?
# # Ans: No

# if we do id(ravi object) and id(shyam object) . will we get same memory ids for both

print(id(ravi_object))
print(id(shyam_obj))


# how to modify an attribute
ravi_object.name = "Ravi Singh"
print(ravi_object.name)