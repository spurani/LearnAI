
# adding attribute dynamically

class EdurekaStudent:
    def __init__(self, a, b, c):
        self.name = a
        self.age = b
        self.course = c
        self.fees = '$300'

    def show_name(celina):
        print(celina.name)


ravi = EdurekaStudent("Ravi singh", 25, 'Py')  # ravi.__init__(ravi)

# adding an user defined attribute dynamically
ravi.sudipta = "hello"
print(dir(ravi))

shyam = EdurekaStudent("Shyam sundar", 28, 'Py')
print(dir(shyam))
