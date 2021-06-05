#1. sorted(iterable)

new_list = sorted([-1, 2, 90, -4, -56])
print(new_list)

new_list = sorted([-1, 2, 90, -4, -56], reverse=True)
print(new_list)

























# new_list = sorted([-1, 2, 90, -4, -56], reverse=True)
# print(new_list)

#2. all() returns True is all the elements are True

# print(all([1,2, "hello", -1, None]))
#
# print(all([1,2, "hello", -1]))
'''
What is True ?
Ans: Any non-zero, non-empty value or True

What is False ?
Ans: False, 0, '', [], (), {} or any empty object, None
'''

# any() returns True is any of the element is True

#print(any(['', [], (), {}, None]))
#print(any(['', [1], (), {}, None]))

#3. bool()
#print(bool(None))

# 4.chr(code_point/ascii_value) returns character tied to that code
#print(chr(97))

# 5. ord(character) returns code point/ASCII value
#print(ord('a'))

# 6. abs()
#print(abs(-189))

# 7. enumerate() is used to iterate over a sequence and get (index, value)

# a = [11, 12, 13, 14, 15]
# for i in a:
#     print(i)
# print("#"*20)
# a = [11, 12, 13, 14, 15]
# for i in enumerate(a):
#     print(i)
# print("$"*20)
# for i, val in enumerate(a):
#     print(i, val)

# 8.int() is used for typecasting
# val = int("123")
# print(type(val))
# print(val)

# 9. globals()
# a = 100
# b = 200
# print(globals())

# 10. bin()
# print(bin(23))

# 11. eval()
# print(eval("1>2"))
# print(type(eval("[1,2,3]")))

# 12. sum(iterable)
# print(sum([1, 2, 3, 4, -1]))
# print(sum((10, 20, 30)))
# print(sum({1: 11, 2: 22}))




