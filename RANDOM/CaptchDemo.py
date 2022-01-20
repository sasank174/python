

import random
import time

for i in range(1,11):
    time.sleep(.5)
    print( random.randint(11,99), chr(random.randint(65,90)), random.randint(11,99) , chr( random.randint(97,122) ),sep='')
