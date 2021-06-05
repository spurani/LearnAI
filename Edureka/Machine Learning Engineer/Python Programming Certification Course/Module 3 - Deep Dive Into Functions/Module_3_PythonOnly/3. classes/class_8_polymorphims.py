# polymorphism


class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        pass


class Cat(Animal):
    def talk(self):
        print("Meow")


class Dog(Animal):
    def talk(self):
        print("Woof Woof")


########### user code ########
c = Cat("kitty")
c.talk()
d = Dog("Tommy")
d.talk()

########## another example ###########
# team lead
class Connection:
    def __init__(self, ip, pwd, username):
        self.ip = ip
        self.pwd = pwd
        self.username = username

    def connect(self):
        raise NotImplementedError("please override this method")


# developer 1
class ConnectionServerA(Connection):
    # overriding the parent class connect() method
    def connect(self):
        print("connected to A")


# developer 2
class ConnectionServerB(Connection):
    # overriding the parent class connect() method
    def connect(self):
        print("connected to B")


############
A = ConnectionServerA('123.45.2.3', 'jhdjvh', 'jhdbvh')
A.connect()
B = ConnectionServerB('123.45.2.3', 'jhdjvh', 'jhdbvh')
B.connect()
