"""
Topics covered:
1.'super' keyword
(is used to call parent's class method from child class)
2. how to deal with the init method if child class also contains
 init method

 Ans: In this case call the Parent's class init method explicitly if you want to use parent
 class attribute

"""
class Rectangle:
    def __init__(self, length, breadth):
        print("Init of Rectangle")
        self.length = length
        self.breadth = breadth
    def get_area(self):
        print("Rectangle area is: ", self.length*self.breadth)

class Square(Rectangle):
    def __init__(self, side):
        print("Init of square")
        # M1
        super(Square, self).__init__(side, side)
        # M2
        #Rectangle.__init__(self, side, side)
        self.side = side

    def get_area(self):
        print("Square area is: ", self.side*self.side)

sq = Square(10)
print(sq.length)

# y not to pass lenght and breadth in line 24 for rectangle class ?

