class Car:
    make = None
    model = None
    year = None
    color = None
    wheel = 4 #this value will be applied to all elements to class

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print(self.model + " is driving")
    def stop(self):
        print(self.model + " is stopped")
