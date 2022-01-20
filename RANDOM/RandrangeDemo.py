
'''
range(10) -> range(0,10) 
randrange(stop) -> randrange object '''

import random
import time

for i in range(1,11):
    time.sleep(.4)
    print( random.randrange(10) )

