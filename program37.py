# Please write a program which accepts basic mathematic expression from console 
# and print the evaluation result.

# Example:
# If the following string is given as input to the program:
# 35+3
# Then, the output of the program should be:
# 38

import re
s = input(">")
print("%s = %d" % (s,eval(s)))