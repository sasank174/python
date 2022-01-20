
''' writer(file) -> writer object  from csv module
    to write the data into CSV | Excel File Then we have to use
   writerow(iterable) method from writer class '''

import csv

with open("d:\\python8\\james\\mystudent1234.csv","w",newline='') as f:
    writer=csv.writer(f)
    writer.writerow(["sno","sname","scity"])

    while True:
        sno=input("Enter sno ")
        sname=input("Enter sname ")
        scity=input("Enter scity ")
        writer.writerow([sno,sname,scity])
        opt=input("Do u want another y|n ")
        if opt in['N','n']:
            break
    
print("Data is Saved")
    

