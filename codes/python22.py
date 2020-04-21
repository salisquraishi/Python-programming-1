# With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values 
# in one line and the last half values in one line. 

t =  (1,2,3,4,5,6,7,8,9,10)

bound = int(len(t)/2)
print(bound)
print("First half:",t[:bound])
print("Second half:", t[bound:])