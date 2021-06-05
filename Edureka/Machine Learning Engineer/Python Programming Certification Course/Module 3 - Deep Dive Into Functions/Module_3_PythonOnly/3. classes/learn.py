"""
if parent and child both contain __init__ methods then if you instantiate the child class then
parent class init method won't be called automatically therefore with the help of super keyword( or
also the other syntax) you would have to explicitly call the parent class init.
"""

class A:
    def __init__(self, a, b):
        print("init parent")
        self.a = a
        self.b = b

    def hello(self):
        print("AA")


class B(A):
    def __init__(self, c, d):
        print("init child")
        #A.__init__(self, c+10, d+10)      # syntax 1 to call parent class method
        super().__init__(c+10, d+20)         # syntax 2(preferred) to call parent class method
        self.c = c
        self.d = d

    def bye(self):
        super().hello()  # calling parent class method
        print("BBBB")


obj = B(1, 2)
print(obj.a)
obj.bye()









