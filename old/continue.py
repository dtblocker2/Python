#terminates execution  in current iteration and continues execution of the loop with the next iteration
#break stops the command while continue skips the condition and continue next operations of the command

i = 0
while i <= 5:
    if i == 3:
        i += 1
        continue #due to this when i=3 next set of commands will be skipped
    print(i)
    i += 1

''' print only odd numbers'''
i = 0
while i <= 10:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1