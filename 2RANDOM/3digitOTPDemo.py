import random
import time

for i in range(1,11):
    time.sleep(.3)
    print(random.randint(0,9) , random.randint(0,9) , random.randint(0,9) ,sep='')
