# Write a program that accepts a sentence and calculate the number of upper case letters 
# and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

sentence = input(">")
uc_count = 0
lc_count = 0

for c in ' '.join(sentence):
    if c.isalpha():
        if c.isupper():
            uc_count += 1
        elif c.islower():
            lc_count += 1

# print result
print("UPPER CASE: ", uc_count)
print("LOWER CASE: ", lc_count)