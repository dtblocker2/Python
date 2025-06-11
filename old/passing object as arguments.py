class car:
    color = None

def change_color(car, new_color):
    car.color = new_color

car_1 = car()
car_2 = car()
car_3 = car()
print(car_1.color)
print(car_2.color)
print(car_3.color)

change_color(car_1, "white")
change_color(car_2, "blue")
change_color(car_3, "black")

print(car_1.color)
print(car_2.color)
print(car_3.color)