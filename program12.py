# Write a program, which will find all such numbers between 1000 and 3000 (both included) 
# such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

lb = 1000
ub = 3000

# result
out = []

for num in range(lb, ub+1):
    skip = 'n'
    for d in str(num).split():
        if not int(d)%2 == 0:
            skip = 'y'
            break
    if skip == 'n': out.append(num)

# print output

print(*out, sep=',')
print("Total count of even numbers betwee %d and %d is: %d" % (lb, ub, len(out)))