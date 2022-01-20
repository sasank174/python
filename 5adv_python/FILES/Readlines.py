
import time

f=open("flowers")
lst=f.readlines()   #lst is the collection of lines 
print(lst)

for line in lst:
    time.sleep(1)
    print(line,end='')
