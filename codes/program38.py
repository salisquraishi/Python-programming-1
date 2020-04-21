# Please write a binary search function which searches an item in a sorted list. 
# The function should return the index of element to be searched in the list.

l = ['apple', 'mouse', 'bottle', 'lamp', 'table', 'swimming']

item = input("search?:")
def look(item):
    for i, v in enumerate(sorted(l)):
        if v == item:
            print("Index: ",i) 

look(item)