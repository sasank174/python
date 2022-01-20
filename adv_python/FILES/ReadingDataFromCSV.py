
''' reader(file) -> csvreader object  is the collection of rows in list
    from csv module '''

import csv
import time

with open("d:\\python8\\james\\mystudent1234.csv","r") as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        time.sleep(1)
        print(row[0],"\t",row[1],"\t",row[2])
    
