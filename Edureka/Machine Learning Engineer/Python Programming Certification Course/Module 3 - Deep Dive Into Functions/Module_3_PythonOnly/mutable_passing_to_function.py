"""
can you please explain usage of global variable within a function in terms
of mutable and immutable/memory blocks
"""

a = [1, 2]  # mutable object
b = [3, 4]


def func(i, j):
    i.append(100)
    j = [4, 5]

# call by value where value is the object reference
func(a, b) #
#func(list(a), list(b)) #
print(a)
print(b)
