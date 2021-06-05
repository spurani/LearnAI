class EdurekaPythonUser:
    def __init__(self, name, gender):
        self.course = 'Python'    # object or instance attributes
        self.name = name
        self.gender = gender


######## client code ###

ravi = EdurekaPythonUser("Ravi", "M")  # ravi.__init__(ravi, "Ravi", 'M')

# access an attribute
print(ravi.gender)
print(ravi.course)
print(ravi.name)

#create an attribute dynamically: not a good programming approach
ravi.mohit = "this attr  mohit is available only for Ravi"
print(ravi.mohit)

# another istance
shyam = EdurekaPythonUser("Shyama", 'F')

#print(shyam.mohit)  # error

