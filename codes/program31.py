# Define a custom exception class which takes a string message as attribute.


ans = input("Do you love coding (yes/no) ?: ")

class MyShowStopper(Exception): pass
def check():
    if ans == 'no':
        raise MyShowStopper()
    elif ans == 'yes':
        print("Fabulous")

try:
    check()
except MyShowStopper:
    print("get lost :(")
