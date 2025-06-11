#adding space after formating
print("hello my name is {name:>10} and nice to meet you".format(name = "dhruva")) #right align
print("hello my name is {name:<10} and nice to meet you".format(name = "dhruva")) #left align
print("hello my name is {name:^10} and nice to meet you".format(name = "dhruva")) #centre align

'''converting one number to different number sytem'''
x = 12000000
print("{:,}".format(x))
print("{:b}".format(x)) #binary
print("{:o}".format(x)) #octal
print("{:x}".format(x)) #hexadecimal
print("{:e}".format(x)) #scienticfic