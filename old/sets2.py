#unlike lists sets and tuples can only store unique values and sets are mutable but its elements are immutable ie we can add or remove elements but we can't change values to elements that's why lists and dictionaries are not allowed in sets (BECAUSE THEY ARE MUTABLE) but tuples are allowed in sets(BECAUSE THEY ARE IMMUTABLE)
lol = {1, 4, 3, "kaku", "kaku"} #it automatically sorts item

#it will ignore duplicate value
print(lol)
print(len(lol)) #its also doesn't count duplicate values

empty_set = set()
print(empty_set)
empty_set.add(1)
empty_set.add(2)
empty_set.add(2)
print(empty_set)
empty_set.remove(1)
print(empty_set)

empty_set.add((1, 4, 3))
print(empty_set)

'''empty_set.add([1, 4, 3])
print(empty_set)''' #error

lol.union(empty_set)
print(lol)

set_1 = {1, 2 , 7}
empty_set.intersection(set_1)

lol.clear()
print(lol)