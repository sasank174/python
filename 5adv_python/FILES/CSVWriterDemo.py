
''' writer(file) -> writer object  from csv module
    to write the data into CSV | Excel File Then we have to use
   writerow(iterable) method from writer class '''

import csv

# f=open("d:\\python8\\james\\mystudent.csv","w") or
with open("d:\\python8\\james\\mystudent.csv","w") as f:
    writerobj=csv.writer(f)
    writerobj.writerow(["sno","sname","scity"])


print("Data is Saved")
    

