# Write a program which accepts a string as input to print "Yes" if the string is "yes" 
# or "YES" or "Yes", otherwise print "No". 
import re
what = input(">")
if re.match('yes',what, re.IGNORECASE):
    print("Yes")
else:
    print("No")

