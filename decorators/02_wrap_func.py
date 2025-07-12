def og_func():
    print('OG Func')

#creating decorator for above func
def new_decorator(original_func):
    def wrap_funct():
        print('code before og func')
        original_func()
        print('code after og func')
    return wrap_funct

k = new_decorator(og_func)
k()

# special syntax for above things
@new_decorator #comment it out when turn it on or off
def og_func2():
    print('this is second og')

og_func2()

# these are mainly ised in web apps or django libraries etc. or learn flask to use them further recommended