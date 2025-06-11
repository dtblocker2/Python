#this function is used when we have to prevent to make a element of a certain class but we can make element of subclass of the class ie

from abc import ABC, abstractmethod
class vehicle(ABC):
    @abstractmethod
    def go(self):
        print("this vehicle has started")

class car(vehicle):
    def stop(self):
        print("this car has stopped")
    def go(self):
        print("this car has started")

class bike(vehicle):
    def drift(self):
        print("this bike is drifting")
    def go(self):
        print("this bike has started")

#vehicle_1 = vehicle() see we can't even assign element to this class
car_1 = car()
bike_1 = bike()

#vehicle_1.go() see .go() command is defined for car_1 and bike_1 but not for vehicle_1 its because we can't make elements of this class but we can make elements of its sub classes i.e. bike and car

car_1.go()
car_1.stop()
bike_1.drift()
bike_1.go()