# # lambda function
#
# # normal func
# def func(a, b):
#     return a + b
#
# print(func(1, 2))
#
# print((lambda a, b:a+b)(10, 20))
#
# # to reuse lambda func
# aa = lambda a, b:a+b
# print(aa(1,4))

# applications of lambda func
# 1.map
a = [1, 2, 3, 4]

print(list(map(lambda elem: elem**2+elem+2, a)))

# 2. filter
print(list(filter(lambda elem: elem>2, a)))

# 3. reduce
from functools import reduce
print(reduce(lambda x, y: x+y,a))
