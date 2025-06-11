lol = "bhavi mera Beta hai"
print(lol.endswith("ai")) #true
print(lol.endswith("kai")) #false
print(lol)
print(lol.capitalize()) #capitalises first word and decapitalises others

print(lol.replace("mera Beta", "meri beti")) #replace character in string
print(lol.find("beta")) #doesn't exist thus it gives -1
print(lol.find("Beta")) #exists so it give index of B in Beta

print(lol.count("e")) #no of times the value entered is repeated