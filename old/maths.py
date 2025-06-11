#numeric value can operate with all arithematic operators
a = 23
b = 44
sum = a+b
diff = a-b

print(sum)
print(diff)

#if we add int and float then result is always float
c = 30
d = 5.0000
#yes d is float not int ie answer is 35.0
print(c+d)

#if we devide two int then ans can be float
print(a/b)

#integer division b//a function sive GIF result of floor(b/a)
e = b//a
print(e, b/a)

#remainder function
A = 3
B = 5
C = 7
D = -2
E = -11
#remainder is neagative only if demoninator is negative there is no effect of numerator on sign of remainder

Q = B%A
V = C%D
F = E%B
P = E%D
print(Q, V, F, P)