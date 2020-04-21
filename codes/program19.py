# Question:
# Define a class with a generator which can iterate the numbers, 
# which are divisible by 7, between a given range 0 and n.

def div_by_7(n):
    for i in range(n+1):
        if i%7 == 0:
            yield i

for num in div_by_7(50):
    print(num)