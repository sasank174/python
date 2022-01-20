
''' iterable object
    str | list | tuple | set | dict | range | file | cursor | callable_iterator '''

import time
r=range(1,11)   # <class 'range'>
for i in r:
    time.sleep(.2)
    print(i)

lst=[10,20,30,"Shashi","Ramesh","Sssit"]
for i in lst:
    time.sleep(.2)
    print(i)
