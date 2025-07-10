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

# Regular function
def contains_i(words):
    i_words = []
    for word in words:
        if 'i' in word:
            i_words.append(word)
    
    return i_words

print(contains_i(some_words))

# generator function
def contains_a(words):
    i_words = []
    for word in words:
        if 'a' in word:
            yield word
k = contains_a(some_words)
print(k) #generator object convert it io list
print(list(k))