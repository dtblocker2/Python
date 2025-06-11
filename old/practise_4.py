#see 9 and 9.0 are treated as same value but to make difference use
set_lol = {2, 9, 9.0}
print(set_lol)

#one of solution is
set_lol = {2, 9, "9.0"}
print(set_lol)

#another solution is making a tuple ie in tuple 9 and 9.0 will be treated differently as int and float respectively
set_lol = {2, ("int", 9), ("float", 9.0)}
print(set_lol)