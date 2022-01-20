''' ReadObjectDemo.py '''

import pickle,time

with open("myeinfo","rb") as f:
    e=pickle.load(f)
    time.sleep(1)
    e.getEmployee()
