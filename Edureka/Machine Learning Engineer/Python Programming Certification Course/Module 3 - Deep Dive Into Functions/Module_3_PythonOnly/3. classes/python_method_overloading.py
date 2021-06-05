"""
Q: Does Python support method overloading or not?
A: No it doesn't

(*args, **kwargs)

"""

class A:
    def add(self, a, b):
        print("11")

    def add(self, a):
        print("22")

    def add(self):   # now previous two add() methods have been overwritten
        print("33")     # only the last method would remain

######
obj = A()
obj.add()

