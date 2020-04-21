# Write a program that computes the net amount of a bank account based a transaction log 
# from console input. The transaction log format is shown as following:
# D 100
# W 200

# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500

# transaction log in tx dictionary
tx = {'d' : {}, 'w' : {}}
tx['d'] = {'1' : 300, '2' : 300, '3' : 100}
tx['w'] = {'1' : 200}

total_d = 0
total_w = 0

for i in tx['d'].keys():
    total_d += tx['d'][i]

for j in tx['w'].keys():
    total_w += tx['w'][j]

# print output
balance = total_d - total_w
print("Balance: %d" % balance)