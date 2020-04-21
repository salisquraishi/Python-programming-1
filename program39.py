# We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
# How many rabbits and how many chickens do we have?


# ckn + rbt = 35
# ckn*2 + rbt*4 = 94 
# i.e ckn + 2*rbt = 47
# 47 - 2*rbt +rbt = 35
# rbt = 47 - 35
# rbt = 12
# ckn = 23

for c in range(35+1):
    for r in range(35+1):
        if eval('c+r') == 35 and eval('c + 2*r') == 47:
            print("Chicken: ", c)
            print("Rabbit: ", r)
