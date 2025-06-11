#to print all keys of a dictionary (nested keys are not included)
student = {
    "name" : "bhavi",
    "subject" : {
        "chemistry" : 99,
        "physics" : 100,
        "maths" : 99
    }
}
print(student.keys())

#to print nested dictionary keys use
print(student["subject"].keys())

#print all keys in form of list
lol = list(student.keys())
print(lol)
print(len(lol))

#to make key:value tuple list
print(student.items())
#we can also access individual key:value pair by conerting it into list and using indexing
pairs = list(student.items())
print(pairs[1])

'''work of student.get("key") and student["key"] is same'''
#use .get command is to prevent error while accessing a key in a dictionary ie

#print(student("name2")) #error
print(student.get("name2")) #None