
import os.path
import time

if os.path.exists("d:\\python8\\lambda\\filterdemo4.py"):
    print("Given path is Existed ")
    with open("d:\\python8\\lambda\\filterdemo4.py","r") as f:
        data=f.read()
        for i in data:
            time.sleep(.1)
            print(i,end='')    
else:
    print("Sorry Path is not existed ")
