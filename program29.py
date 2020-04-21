# Define a class named Shape and its subclass Square. 
# The Square class has an init function which takes a length as argument. 
# Both classes have a area function which can print the area of the shape 
# where Shape's area is 0 by default.

class Shape():
    def __init__(self):
        pass

    def area(self):
        self.area = 0
        print(self.area)

class Square(Shape):
    def __init__(self, l):
        self.length = l

    def area(self):
        self.area = self.length*self.length
        print(self.area)

sq1 = Shape()
sq1.area()

sq2 = Square(4)
sq2.area()
