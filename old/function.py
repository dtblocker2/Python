''' def func_name(param1, param2, param3.....):
    <some work>
    return val
func_name(arg1, arg2, arg3.....)''' #function call

def multi(a, b, c):
    p = a*b*c
    print(p)
    return p #return mean output taht we want to provide

multi(2, 3, 5)
multi(4, 5,22)
multi(22, 33, 51)

#assigning default values when no argument for a parameter is not given
def sum(a = 0, b = 0, c = 1):
    s = (a+b)/c
    print(s)
    return s
sum(2, 5)