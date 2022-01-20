
def myFun():
    yield 10

g=myFun()
print("Type is ",type(g))
print(g)

import time
t=(i for i in range(1,11))
print("Type is : ",type(t))
print("values : ",t)
for i in t:
    time.sleep(1)
    print(i)
