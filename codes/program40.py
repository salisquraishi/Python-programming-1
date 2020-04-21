# Please write a program which prints all permutations of [1,2,3]

from itertools import permutations
l = [1,2,3]
for p in permutations(l): print(p)