# if return statement is executed then remaining code in that function..
# ... wouldn't be executed


def add(a, b):
    c = a + b
    return c
    print("I am not reachable")


val = add(100, 200)
print(val)

