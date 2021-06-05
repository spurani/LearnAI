"""
Python 3.x
1.Abstract classes used to define the API names
3. In abstract class the abstract methods present would not be having a body, the body must be defined
in the child class.
3. in child class all the abstract methods must be overridden.
4. An abstract class can have non-abstract methods also
"""
from abc import ABC, abstractmethod


# Team leader
class Connection(ABC):  # inherting ABC class makes a class an abstract class

    @abstractmethod
    def connect(self):
        # as this is an abstract method therefore it must be overridden in the child class
        pass

    @abstractmethod
    def close(self):
        # as this is an abstract method therefore it must be overridden in the child class
        pass

    def hello(self):
        # as this is not an abstract method therefore it needn't to be overridden in the child class.
        pass

# Ravi
class ServerAConnection(Connection):
    def connect(self):
        # connect to server code
        print("connect is overridden here")

    def close(self):
        print("close overridden here")

    def bye(self):
        print("edureka")

# user code
a = ServerAConnection()
print(a)
