food = "Daal Bhati"
place = "circuit house"
print("I ate {0} at jaipur".format("roti"))
print("I ate {0} at jaipur and went to {1}".format(food, place))
print("I ate {1} at jaipur and went to {0}".format(food, place))
print("my favourite animal is {animal}".format(animal="wolf"))

#efficient way
text = "Your name is {1} and your age is {0}"
age = int(input("enter your age:"))
name = input("enter your name:")
print(text.format(age, name))