#-------------------------------------------------------------------------------------------------------
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
#------------------------------------------------------------------------------------------------------

num = range(2000, 3200+1)
result = []
denom1 = 7
denom2 = 5

for item in num:
    if (item%denom1 == 0) and (item%5 != 0):
        result.append(item)

#print(*result, sep=',')
print(','.join(map(str,result)))