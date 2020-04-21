# A website requires the users to input username and password to register. 
# Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1
import re
pwd = input("Enter Password>")
# validation funtion to check all constraints mentioned in the problem statement
def validate(pwd, good = 'y'):
    upper_flag = 'n'
    spcl_flag = 'n'

    if (len(pwd) < 6 or len(pwd) > 12):
        print("Length of the password should be minimum 6 character or maximum 12 characters long")
        good = 'n'
        pass

    elif pwd.lower().isalpha():
        print("Password should contain at least one alphabate character")
        good = 'n'
        pass

    elif pwd.isdigit():
        print("Password should contain at least one numeric character")
        good = 'n'
        pass 

    for c in pwd:
        if re.match('[A-Z]', c):
            upper_flag = 'y'

        if re.match('[$@#]', c):
            spcl_flag = 'y'

    if upper_flag == 'n':
        print("At least one upper case character required")
        good = 'n'
        pass

    if spcl_flag == 'n':
        print("At least one character needs to be #, @ or #")
        good = 'n'
        pass

    return good

# call validate function
good = validate(pwd)
if good == 'y': print("Awesome !!, your password is set")