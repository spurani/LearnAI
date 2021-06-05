class Edureka:
    def __init__(self, courseName):
        self.courseName = courseName

    def getter_courseName(self):
        return self.courseName

    def setter_courseName(self, new_val):
        self.courseName = new_val

########## user code###

obj = Edureka("Python")
# print(obj.courseName)  # access
# obj.courseName = "Django"  # modifying
# print(obj.courseName)

print(obj.getter_courseName())
obj.setter_courseName("Django")
print(obj.getter_courseName())
