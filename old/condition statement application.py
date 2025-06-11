color = input("color of traffic light? ")

# single = is used to assign values to variables and double == are used to check similarity see below
if color == "red":
    print("stop")
elif color == "yellow":
    print("wait")
elif color == "green":
    print("go")
else:
    print("papa", color, "rang ki light lagwake aaya tha")