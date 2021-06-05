# if return statement is executed then remaining code in that function..
# ... wouldn't be executed


def hello(a):
    if isinstance(a, str):
        return a + " bingo"
    elif isinstance(a, int):
        return a + 1000
    elif isinstance(a, list):
        a.append("appended new value")
        return a
    else:
        return ("this type is not supported")


####### calling
val = hello([1,2])
print(val)

