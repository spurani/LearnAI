class A:
    def hello(self):
        print("Hello AAA")

    def bye(self):
        print("BYEEEEE")


class B(A):
    # hello method is overridden here
    def hello(self):
        print("hi!! BB")


b = B()
b.hello()
b.bye()
