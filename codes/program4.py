# Write a program which accepts a sequence of comma-separated numbers from console 
# and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

input_list = input("Enter: ").split(',')
input_tuple = tuple(input_list)
print(input_list, "\n", input_tuple)

