''' WriteObjectDemo.py '''

import mymodule
import time
import pickle

e=mymodule.Employee()
e.setEmployee()

with open("myeinfo","wb") as f:   # f=open("myeinfo","wb")
    pickle.dump(e,f)

time.sleep(1)
print("Object Is Saved In The File ")
    
