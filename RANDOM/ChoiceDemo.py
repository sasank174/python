
''' choice(iterable) -> item '''

import random,time

lst=["oracle","java","python","django","DS","DA"]

for i in range(1,11):
    time.sleep(.5)
    print( random.choice(lst) )

