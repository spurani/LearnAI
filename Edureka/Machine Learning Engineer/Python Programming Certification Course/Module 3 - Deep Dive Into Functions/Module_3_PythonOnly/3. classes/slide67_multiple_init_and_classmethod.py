"""
class method:
-By putting the in-built decorator @classmethod makes a method
a class method.
- Class method would take first parameter as class whenever it is called.
- It can be called by both object as well as Class name, however it
should be called with class Name only.
"""

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def dmy(cls, day, month, year):
        return cls(year, month, day) # object of the class Date

    @classmethod
    def mdy(cls, month, day, year):
        return cls(year, month, day)  # object of the class Date

a = Date(2018, 2, 21)

b = Date.dmy(28, 2, 2017)


c = Date.mdy(12,31, 2016)
print(c.year)

# it means that we can pass parameter in any sequences using class method