import random
print("What is your name?")
name = input()
print("Hello, "+name+"!")

print("Rolling the dice...")
d1 = random.randint(1,6)
d2 = random.randint(1,6)
sum = d1 + d2
print("Die 1: "+str(d1))
print("Die 2: "+str(d2))
print("Total value: "+str(sum)) 
if sum > 7:
    print(name+" won!")
else:
    print(name+" lost") 