class Edureka:
    def __init__(self):
        self.pub = "public attribute"
        self._prot = "protected attr"
        self.__pri = "private attr"

        self.__magic_no = .10 # 10%

    def calculate_lumpsum(self, investment_amount, years):
        print( investment_amount + years*self.__magic_no*investment_amount)

    def __private_my_method(self):
        print("Private method")

    def method2(self):
        self.__private_my_method()
        print("calling private attr without name mangling:", self.__pri)



### client code  #
obj = Edureka() # it would call init method

print(obj.pub)
#print(obj.__magic_no)

# name mangling for private attribute is done

print(obj._Edureka__magic_no)

# private method is also accessed via mangled name

# obj.__private_my_method()  # Won't work
obj._Edureka__private_my_method()  # Will work

obj.method2()


"""
self.pub and self.prot is created in INIT method, how come call it in out side of that  method?
similar like can we create these variables from other methd as well?
"""
