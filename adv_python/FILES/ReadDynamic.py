
import time

f=None  #global variable

try:
    fname=input("Enter Filename ") #James
    f=open(fname,"r")
except FileNotFoundError:
    print("File Not Found ")
else:
    data=f.read()
    for i in data:
        time.sleep(.1)
        print(i,end='')
finally:
    if f!=None:
        f.close()
