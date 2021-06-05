# api
def func(*args, **kwargs):
    print("Positional params:", args)
    print("Keyword params:", kwargs)


# client code
#valid calls
func()
func(1, 2)
func(a=12, b=13)
func(1, 2, a=12, b=13)

# # invalid calls
# func(a=12, 12) # cannot provide positional args, after keyword args
# func(12, 13, b=14, 15)

# RULE
# if you have both keyword and positional arguments then firstly put all the positional args then...
# ...only put the keyword arguments in any order


