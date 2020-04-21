# Assuming that we have some email addresses in the "username@companyname.com" format, 
# please write program to print the user name of a given email address. 
# Both user names and company names are composed of letters only.

import re
email = input("Email please>")

match = re.match('^(\w+)@.*', email)

print("User name is:", match.group(1))
