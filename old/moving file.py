'''import os

source = "C:\\Users\\dhruv\\OneDrive\\Desktop\\pythonProject\\chapter-8\\test_3.txt"
destination = "C:\\Users\\dhruv\\OneDrive\\Desktop\\test_3.txt"

try:
    if os.path.exists(destination):
        print("file already present with this name")
    else:
        os.replace(source,destination)
        print(source + " was moved")

except FileNotFoundError:
    print("no file present with name test_3")'''

import os

destination = "C:\\Users\\dhruv\\OneDrive\\Desktop\\pythonProject\\chapter-8\\test_3.txt"
source = "C:\\Users\\dhruv\\OneDrive\\Desktop\\test_3.txt"

try:
    if os.path.exists(destination):
        print("file already present with this name")
    else:
        os.replace(source,destination)
        print(source + " was moved")

except FileNotFoundError:
    print("no file present with name test_3")