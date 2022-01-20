
import time

f=None  #global variable

try:
    filename=input("Enter File name ") #super
    f=open(filename,"r")
except FileNotFoundError :
    print("Sorry File Not Found ")
else:
    data=f.read()
    for i in data:
        time.sleep(.05)
        print(i,end='')
finally:
    if f!=None:
        f.close()
