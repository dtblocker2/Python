class organism:
    alive = True

class animal(organism):
    def eat(self):
        print("this animal is eating")
        return self #this line is imp for method chaining

class dog(animal):
    def bark(self):
        print("it can bark")
        return self
    def run(self):
        print("it can run very fast")
        return self

#the class will overwrite its parent class function if another function of same name is made in it it is called "overwritting of function"
class cat(animal):
    def eat(self):
        print("it doesnt want to eat")

dog = dog()
cat = cat()

dog.bark()
print(dog.alive)
dog.eat()
cat.eat()

#method chaining
print("------------------------------------------")
dog.eat().bark().run()