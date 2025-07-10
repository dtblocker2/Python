# normal function that returns list will show momory error due to excessive memory taken but generator function won't or take a lot of memory about 9 GB in my computer
'''
def nums():
    i=0
    num=[]
    while True:
        num.append(i)
        i+=1

nums()
'''

# below function only take 650 MB as memory though it is increasing slowly with time to 950 MB and above
def nums2():
    i=0
    while True:
        yield i
        i+=1

for k in nums2():
    print(k)