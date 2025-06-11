shape = input("What is the shape?")

if shape == "square":
    s = float(input("what is side length?"))
    A = s ** 2
elif shape == "rectangle":
    l = float(input("what is length?"))
    b = float(input("what is breadth?"))
    A = l * b
elif shape == "circle":
    r = float(input("what is its radius"))
    A = 22/7*r**2
elif shape == "ellipse":
    a = float(input("what is its major axis"))
    b = a = float(input("what is its minor axis"))
    A = 22/7*a*b
elif shape == "yo mama":
    A = "infinity"
else:
    A = "I don't know its area"

print(A)