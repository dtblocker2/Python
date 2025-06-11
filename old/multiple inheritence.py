class prey:
    def flee(self):
        print("it is running")

class predator:
    def hunt(self):
        print("it is hunting")

class rabbit(prey):
    pass
rabbit = rabbit()

class hawk(predator):
    pass
hawk = hawk()

class fish(prey, predator):
    pass
fish = fish()

rabbit.flee()
fish.hunt()
fish.flee()
hawk.hunt()