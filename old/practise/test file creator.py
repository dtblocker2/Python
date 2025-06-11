import os
import time

x = 0

while True:
    x = str(x)
    file_path = "test_" + x +  ".py"
    if not os.path.isfile(file_path):
        with open(file_path, 'w') as file:
            file.write("#this is new python file")
        break
    else:
        x = int(x)
        x += 1

x = str(x)
print("test_" + x + " created succesfully")
time.sleep(5)