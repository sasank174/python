
import time

f=open("flowers","r")
data=f.read()
for i in data:
    time.sleep(.1)
    print(i,end='')
