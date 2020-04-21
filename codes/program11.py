# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input 
# and then check whether they are divisible by 5 or not. 
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010

# get sequence of binary input from user
b = input("Enter: ").split(',')
out = [] # to hold output number which is divisible by 5
# check if input is valid binary 4 digit input
for item in b:
    if len(item) != 4:
        print("Number %s is not a 4 digits long, try again" % item)
        exit()
    elif not item.isdigit():
        exit("Not a number")
    else:
        for d in list(item):
            try:
                int(d)
            except ValueError:
                print("Not an integer value")
                exit()
            
            if not ((int(d) == 0) or (int(d) == 1)):
                print("Not a binary")
                exit()

for num in b:
    if int(num,2)%5 == 0: out.append(num)

# print output
print(','.join(out))