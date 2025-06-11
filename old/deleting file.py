# os.remove(file) ==> removes file
# os.rmdir(directory) ==> removes only empty directory
# shutil.rmtree ==> removes non empty as well as empty directory

'''import os
path = "C:\\Users\\dhruv\\Desktop\\pythonProject\\chapter-8\\test_4.txt"
try:
    os.remove(path)
    print("file deleted successfully")
except FileNotFoundError:
    print("file is already deleted")'''

'''import os
#you can delete file easily but to delete empty file directory use
lol = "C:\\Users\\dhruv\\Desktop\\pythonProject\\chapter-8\\empty_folder"
try:
    os.rmdir(lol)
    print("folder deleted successfully")
except FileNotFoundError:
    print("folder already deleted")'''

import os
import shutil
#to delete a non empty folder use
lol = "C:\\Users\\dhruv\\Desktop\\pythonProject\\chapter-8\\non_empty_folder"
try:
    shutil.rmtree(lol)
    print("file directory deleted successfully")
except FileNotFoundError:
    print("it is already deleted")