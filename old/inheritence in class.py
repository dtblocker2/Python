class Animal:
    alive = True
    def eat(self):
        print("This animal is eating")
    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):
    def run(self):
        print("It can run")
class Fish(Animal):
    def swim(self):
        print("It can swim")
class Hawk(Animal):
    def fly(self):
        print("It can fly")

#-----------------------------------
Hawk = Hawk()
Rabbit = Rabbit()
Fish = Fish()
#------------------------------------

Hawk.sleep()
Fish.eat()
print(Rabbit.alive)
Fish.swim()
Hawk.fly()
Rabbit.run()