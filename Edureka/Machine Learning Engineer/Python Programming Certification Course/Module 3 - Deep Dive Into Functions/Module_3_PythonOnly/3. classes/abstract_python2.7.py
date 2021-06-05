"""
Python 2.7
1.Abstract classes used to define the API names
3. the abstract methods would not be having a body
3. in child class all the abstract methods must be overridden.
4. An ABC can have non-abstract methods also
"""
from abc import ABCMeta, abstractmethod

# Team leader
class Connection:
    __metaclass__ = ABCMeta  # this makes a class an abstract class

    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def close(self):
        pass
    def hello(self):
        pass

# Ravi
class ServerAConnection(Connection):
    def connect_A(self):
        """
        :return:
        """
        #kjdn
        ##mndkfbjg

    def connect(self):
        # connect to server code
        pass
    def close(self):
        pass


# user code
a = ServerAConnection()
