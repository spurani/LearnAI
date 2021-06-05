"""
if parent and child both contain __init__ methods then if you instantiate the child class then
parent class init method won't be called automatically therefore with the help of super keyword( or
also the other syntax) you would have to explicitly call the parent class init.
"""

"""

class Employee:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def show_name(self):
        print(self.name)


class Developers(Employee):
    def __init__(self, no_of_defects, name, gender):
        self.no_of_defects = no_of_defects
        #super(Developers, self).__init__(name, gender)  # syntax 1 to call parent class method
        #Employee.__init__(self, name, gender)      # syntax 2 to call parent class method
        super().__init__(name, gender)         # syntax 3 :(preferred) to call parent class method

############

dev_obj = Developers(10, "Ravi singh", 'Male')

print(dev_obj.name)

"""
class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def hello(self):
        print("AA")


class B(A):
    def __init__(self, c, d):
        #A.__init__(self, c+10, d+10)      # syntax 1 to call parent class method
        super().__init__(10, 20)         # syntax 2(preferred) to call parent class method
        self.c = c
        self.d = d

    def bye(self):
        super().hello()  # calling parent class method
        print("BBBB")


b = B(1, 2)
print(b.a)
b.bye()
