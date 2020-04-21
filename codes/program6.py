# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24
import math
C = 50
H = 30

out = []
D = map(int, input("Enter:").split(','))
for i in D:
    n = math.sqrt((2*C*i)/H)
    out.append(round(n,2))

print(out) 
    