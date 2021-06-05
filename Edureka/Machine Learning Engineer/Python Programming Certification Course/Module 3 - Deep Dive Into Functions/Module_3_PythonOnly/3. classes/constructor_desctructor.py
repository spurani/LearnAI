class Edureka:
    def __init__(self):
        print("INIT called")

    # used for cleanup actions
    def __del__(self):
        print("object is going to be deleted, used for clean up actions")

obj = Edureka()
#del obj
print("END")
# If object is deleted then second stmt del
# obj should give some error, if not then wht it is deleting??
