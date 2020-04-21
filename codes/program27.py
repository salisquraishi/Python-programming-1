# Define a class named Circle which can be constructed by a radius. 
# The Circle class has a method which can compute the area. 

class Circle():
    def __init__ (self,r):
        self.area = 3.14*(r*r)
        print("Area of a circule with radius %d is: %f" % (r, self.area))

a = Circle(4)