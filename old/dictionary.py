#dictionary are used to store values in key:value pairs. they are unordered, changeable and doesn't allow duplicate pairs
dic = {
    "name" : "Dhruva",
    "class" : 12,
    "learning" : "python",
    "subjects" : ["physics", "chemistry", "maths"]
}

print(dic)

#to access a value of dictionary use
print(dic["name"])

#to add new key and its value in a dictionary use a new name for key
dic["room"] = 11
print(dic)

#to change data in dictionary use
dic["name"] = "kaku"
print(dic)

#we can also make null dictionary
empty_dictionary = {

}
print(empty_dictionary)
#now we can also add key and its value to this null dictionary
empty_dictionary["money"] = 0
print(empty_dictionary)