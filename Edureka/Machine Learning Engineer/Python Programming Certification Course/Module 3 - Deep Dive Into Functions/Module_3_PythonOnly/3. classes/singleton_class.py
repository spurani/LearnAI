"""
singleton class is based on a singleton design pattern in which only
one instance can be created for a class
"""

class MySingleton:
    _instance = None
    def __new__(self):
        if self._instance is None:
            self._instance = super(MySingleton, self).__new__(self)
            self.y = 100
        return self._instance


obj1 = MySingleton()
print(obj1)

obj2 = MySingleton()
print(obj2)

print(obj1 is obj2)