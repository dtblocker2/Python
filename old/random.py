import random

x = random.randint(1,30)
y = random.random()
mylist = ["rock", "paper", "scissors"]
z = random.choice(mylist)

print(x)
print(y)
print(z)

#using shuffle
cards = [1,2,3,4,5,6,7,8,9,10,"A","K","Q","J"]
random.shuffle(cards)
print(cards)