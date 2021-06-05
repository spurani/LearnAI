# variable length args

def func(*args, **kwargs):
    """
    :param args: capture all the positional(required) arguments
    and stores in a tuple.
    :param kwargs: capture all the keyword(non-positional) arguments
    and stores in a dictionary
    """
    print("Positional args:", args)  # as a tuple
    print("keyword args:", kwargs)   # as a dict
    sum = 0
    for elem in args:
        sum += elem
    for elem in kwargs.values():
        sum += elem
    print(sum)


###### client code /api user ##
func()
func(1, 2)
func(1, 2, 3, a=12, b=13)

print((lambda *args, **kwargs: sum(list(args) + list(kwargs.values())))(1, 2, 3,a=12, b=13))
