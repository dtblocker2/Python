from class_module import Car

car_1 = Car("Dodge", "Challeger",2024, "Black")
car_2 = Car("BMW", "Z4", 2005, "Grey")

print(car_1.make, end = " ")
print(car_1.model)
print(car_1.year)
print(car_1.color)
print(car_1.wheel)

print(car_2.make, end = " ")
print(car_2.model)
print(car_2.year)
print(car_2.color)
# to cahnge data of particular element use car_2.wheel = 2
print(car_2.wheel)

car_1.drive()
car_1.stop()
car_2.drive()
car_2.stop()