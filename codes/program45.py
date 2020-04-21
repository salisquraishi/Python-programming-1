# Please write a program to generate all sentences where subject is in ["I", "You"] 
# and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

# I shuffled it so that I don't see robotic output
import random
sentence = []
for s in ["I", "You"]:
    for v in ["Play", "Love"]:
        for o in ["Hockey","Football"]:
            sentence.append(s + ' ' + v + ' ' + o)

random.shuffle(sentence)
for s in sentence: print(s)