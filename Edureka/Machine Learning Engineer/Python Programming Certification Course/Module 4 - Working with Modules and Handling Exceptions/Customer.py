class Customer:
    title = ""
    fname = ""
    lname = ""
    isblacklisted = 0;

    def __init__(self):
        self.title = ""

    def __str__(self):
        return "Title:" + self.title + " First Name:" + self.fname + " Last Name:" + self.lname + " Blacklisted:" + self.isblacklisted

    def setIsblacklisted(self,isblacklisted):
        self.isblacklisted = isblacklisted

    def isblacklisted(self):
        return self.isblacklisted

    def setTitle(self,title):
        self.title = title

    def getTitle(self):
        return self.title

    def setFname(self,fname):
        self.fname = fname

    def getFname(self):
        return self.fname

    def setLname(self,lname):
        self.lname = lname

    def getLname(self):
        return self.lname

customer1 = Customer()
customer1.setTitle("Mr.")
customer1.setFname("Barack")
customer1.setLname("Obama")
#customer1.setIsblacklisted("1")

customer2 = Customer()
customer2.setTitle("Mrs.")
customer2.setFname("George")
customer2.setLname("Bush")
#customer1.setIsblacklisted("0")

# print("First Customer Title %s" , customer1.getTitle())
# print("Second Customer Title %s" , customer2.getTitle())
# print("First Customer Title %s" , customer1.getTitle())

# print("First Customer Title %s" , customer1.getFname())
# print("Second Customer Title %s" , customer2.getFname())
# print("First Customer Title %s" , customer1.getFname())

# print("First Customer Title %s" , customer1.getLname())
# print("Second Customer Title %s" , customer2.getLname())
# print("First Customer Title %s" , customer1.getLname())

#print("First Customer Title %s" , customer1.isblacklisted())
#print("Second Customer Title %s" , customer2.isblacklisted())
#print("First Customer Title %s" , customer1.isblacklisted())
