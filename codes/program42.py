# Define a class Person and its two child classes: Male and Female. All classes have a method 
# "getGender" which can print "Male" for Male class and "Female" for Female class.

class Person():
    def __init__ (self, sex):
        self.gender = sex

    def getGender(self):
        print(self.gender)

class Male():
    def getGender(self):
        self.gender = 'Male'
        print(self.gender)

class Female():
    def getGender(self):
        self.gender = 'Female'
        print(self.gender)

p1 = Person('Male')
p1.getGender()

p2 = Male()
p2.getGender()


p3 = Female()
p3.getGender()