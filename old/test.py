#use the custom module we create use
'''import custom_module
custom_module.hello("Dhruva")
custom_module.add(2,3)'''

'''#for convinience we can use
import custom_module as mod
#now see this
mod.hello("DK")
mod.add(2,3)'''

#also if you want to import specific function
from custom_module import hello
hello("DK")
#see it is not defined add(2,3)