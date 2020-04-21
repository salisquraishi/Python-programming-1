# A robot moves in a plane starting from the original point (0,0). 
# The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
# The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2

# The numbers after the direction are steps. 
# Please write a program to compute the distance from current position 
# after a sequence of movement and original point. If the distance is a float, 
# then just print the nearest integer.
# 
# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2

import math

# get steps
while True:
    try:
        up = int(input("UP>"))
        down = int(input("DOWN>"))
        left = int(input("LEFT>"))
        right = int(input("RIGHT>"))
        print("Thanks")
        break

    except ValueError:
        print("Enter something and only interger please")
        continue

    except EOFError:
        break
        

curr_loc = [0,0]
def traverse(up=0, down=0, left=0, right=0):
    curr_loc[1] += up
    curr_loc[1] -= down
    curr_loc[0] -= left
    curr_loc[0] += right

def dist(loc):
    return round(math.sqrt(loc[1]**2 + loc[0]**2))

# call traverse
traverse(up, down, left, right)
print("current location: ", curr_loc)

# calculate distance
d = dist(curr_loc)

# print 
print("Distance from origin: ", d)