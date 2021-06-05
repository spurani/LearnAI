"""
1.class method:
- By putting the in-built decorator @classmethod makes a method
a class method.
- Class method would take first parameter as class whenever it is called.
- It can be called by both object as well as Class name, however it
should be called with class Name only.

2. static method
- no extra parameter like self or cls is passed to this method
"""


class Edureka:
    i = 100

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def square(val):
        return val**2

    @classmethod  # first param would be class
    def cube(cls, val):
        return val**3 + cls.i
        #myobject=cls(23, 67)
        #return myobject


###
obj = Edureka(10, 20)

output = obj.square(8)  # obj.square(8)
print(output)

val=obj.cube(8)  # obj.cube(Edureka, 8)
print(val)


# class and static methods can be called without object, can be called with class name
Edureka.square(2)
Edureka.cube(3)




