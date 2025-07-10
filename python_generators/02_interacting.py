some_words = [
    "Ben Tennyson", 
    "Goku", 
    "Vegeta", 
    "Light Yagami", 
    "L (Lawliet)",
    "Monkey D. Luffy",
    "Roronoa Zoro", 
    "Naruto Uzumaki", 
    "Sasuke Uchiha", 
    "Tyson Granger"  
]

def contains_a(words):
    i_words = []
    for word in words:
        if 'a' in word:
            yield word
genObj = contains_a(some_words)

# Convert type
print(set(genObj))
print(list(genObj)) #we don get it because genObj is exhausted by previous line
print(tuple(contains_a(some_words)))
print(list(contains_a(some_words)))

# loop
gen_obj = contains_a(some_words)

for el in gen_obj:
    print(el)

# next()
gen_obj = contains_a(some_words)
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
'''print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))'''
# stopIterationError : occurs when we call next more than element in gen_obj