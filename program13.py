# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

# take multiline user input
# one can use sys.readlines as well
sentence = []
while True:
    try:
        s = input()
        if s: sentence.append(s)
    except EOFError:
        break

sentence = ' '.join(sentence)
print("Input sentence is: %s" % sentence)

lcount = 0
dcount = 0
for c in sentence:
    if c.isdigit(): 
        lcount += 1
    elif c.isalpha(): 
        dcount += 1

print("LETTERS:", lcount)
print("DIGITS:", dcount)

