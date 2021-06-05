class Edureka:
    def method(self):
        print("Inside: ", self)
        print(" i am a method")

    def method2(self):
        self.method()


# self is the reference to the object
# client code or api user code

# creating the object or instantiation
obj = Edureka()
print("Outside: ", obj)
obj.method2()  # obj.method2(obj)