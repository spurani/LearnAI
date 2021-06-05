"""
super keyword: used to call parent class method from child class
baseclass, parent class, super class are synonyms
derived, Child and sub-class are synonyms
"""

class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def api(self, i):
        return i**2 + self.a + self.b

class Dinesh(A):

    # Dinesh wrapper above api()
    def api(self, i):
        #out = super(Dinesh,self).api(i) # method 1 to call parent class method
        out = A.api(self, i) # method 2 to call the parent class method
        return out**2

obj = Dinesh(1, 2)
out = obj.api(2)
print(out)
print("#####")
out = obj.api(2)
print(out)
