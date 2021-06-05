# any attribute starting with self is an instance attr
class Edureka:
    a = "class variable"   # can be accessed via class or obj

    def __init__(self, n):
        self.name = n  # name is an instance/object attr
        self.dept = "Data science"


ravi = Edureka("Ravi Sharma")
shyam = Edureka("Shyam Sundar")

# accessing instance variable.
# print(ravi.name)
# print(shyam.name)
# #
# # class var can be accessed via class or objects
# print(ravi.a)
# print(shyam.a)
# print(Edureka.a)  # prefered way to access class var
#
# print("#"*10)
# class var can only be modified by class name
# Edureka.a = 'new value'
# print(ravi.a)
# print(shyam.a)
# print(Edureka.a)
# print("###################")
# don't ever try to modify a class variable using an object
ravi.a = "ravi has tried to modify the class variable"
print(ravi.a)
print(shyam.a)
print(Edureka.a)
print(ravi.__dict__)
print(shyam.__dict__)