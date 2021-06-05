"""
# single inheritance

class A:
    def method(self):
        print("AAAA")

class B(A):
    def hello(self):
        print("BBB")


b = B()
b.method()

"""

"""
# multiple inheritance

class A:
    def hello(self):
        print("AAA")
    def method(self):
        print("11111")

class B:
    def bye(self):
        print("BBB")
    def method(self):
        print("2222")


class C(B, A):
    pass

c = C()
c.bye()
c.method()
print(C.mro())
print(C.__mro__) #method resolution order

"""

# multi-level inheritance

class A:
    def method(self):
        print("AAAA")

class B(A):
    def hello(self):
        print("BBB")

class C(B):
    def bye(self):
        print("CCC")

c = C()
c.method()







