# Write a program that accepts sequence of lines as input and prints the lines 
# after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

# get input lines
lines = []
print("Enter your lines: ")
while True:
    try:
        l = input()
    except EOFError:
        break

    lines.append(l)

# print upper case lines
for l in lines: print(l.upper())
