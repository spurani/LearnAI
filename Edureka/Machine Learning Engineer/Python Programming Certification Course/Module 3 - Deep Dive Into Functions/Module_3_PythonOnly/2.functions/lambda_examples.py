"""
lambda functions
"""
#
# def add(a,b):
#     return a+b
#
# print(add(1,2))
#
# # equivalent lambda function
# out = (lambda a,b:a+b)(1,2)
# print(out)

# Application of lambda function

#####################################
"""
# 1.map(func_obj, sequence)
a = [1, 2, 3, 4]
# what I want is [1, 4, 9, 16]..
print(map(lambda elem: elem**2, a))
print(list(map(lambda elem: elem**2, a)))
print("internally map is doing this:")
print([(lambda elem:elem**2)(1), (lambda elem:elem**2)(2), (lambda elem:elem**2)(3),
 (lambda elem: elem ** 2)(4)])

# doing the same thing using a orthodox 'def' keyword func

def square(i):
    return i**2
print(list(map(square, a)))
"""

#######################################
# 2. filter(function_should_return_boolean_op, iterable)
# filter would consider only those values for which function returns True

# data = [1, 2, 3, 4, 5,6]
# print(filter(lambda elem:elem > 3, data))
# print(list(filter(lambda elem:elem > 3, data)))

########################
# 3. reduce
from functools import reduce

# calculating sum of the sequence
print(reduce(lambda i, j: i+j, [1, 2, 3, 4, 5]))


