import sys

doubles_lc = [num*2 for num in range(1,10000)]
doubles_ge = (num*2 for num in range(1,10000))

print(sys.getsizeof(doubles_lc)) #85176
print(sys.getsizeof(doubles_ge)) #200

import cProfile
print(cProfile.run('max([num*2 for num in range(1,10000)])')) # 4 function call in 0.001 second
print(cProfile.run('max((num*2 for num in range(1,10000)))')) # 10004 function call in 0.002 seconds