#lists are used to  store multiple variables or various datatypes
marks = [94, 93, 87, 82, 76, 68, "kaku"]
print(marks)
print(type(marks))

#similar to string index we can also access values in list by indexing
print(marks[6])
print(marks[5:7]) 
'''slicing of list is also possible'''

#lists are changable ie
marks[0] = 96.8
print(marks) #see its data has now changed

#list methods
lol = [2, 1, 3]

lol.reverse() #reverses order of current list
print("1.", lol)

lol.sort()
print(lol)

lol.sort(reverse = True)
print(lol)

lol.append(4) #add only one elment at end
print(lol)

lol.insert(2, "kaku") #insert element at particular index lol.inser(idx, el)
print(lol)

lol_2 = [1, 2, 3, 2, 4]
lol_2.remove(2) #remove first occurence of 2 in list
print(lol_2)

lol_3 = [1, 2, 3, 5, 9]
lol_3.pop(4) #removes element at idx
print(lol_3)