''' copyfile() ==> copies a file
    copy() ==> copyfile()+permission mode + destination can be directory/folder
    copy2() ==> copy() + copies metadata
'''
import shutil

shutil.copyfile('C:\\Users\\dhruv\\OneDrive\\Desktop\\pythonProject\\chapter-8\\test_2.txt', 'C:\\Users\\dhruv\\OneDrive\\Desktop\\pythonProject\\chapter-8\\copy.txt')