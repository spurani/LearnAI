class A:
    pass


class Edureka(A):
    """
    this is a
    edureka class
    """

    var = 100
    def func(self):
        pass


#1. __dict__
print(Edureka.__dict__)

#2. __doc__
print(Edureka.__doc__)

#3. __name__
print(Edureka.__name__)

#4. __module__
print(Edureka.__module__)

#5. __bases__
print(Edureka.__bases__)
