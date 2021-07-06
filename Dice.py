import random
print("Rolling the dice...")
d1 = random.randint(1,6)
d2 = random.randint(1,6)
sum = d1 + d2
print("Die 1: "+str(d1))
print("Die 2: "+str(d2))
print("Total value: "+str(sum)) 
if sum > 7:
    print("You won")
else:
    print("You lost") 