
''' writer(file) -> writer object  from csv module
    to write the data into CSV | Excel File Then we have to use
   writerow(iterable) method from writer class '''

'''Character	Meaning
'r'     	open for reading (default)
'w'     	open for writing, truncating the file first
'x'     	create a new file and open it for writing
'a'     	open for writing, appending to the end of the file if it exists
'b'     	binary mode
't'     	text mode (default)
'+'     	open a disk file for updating (reading and writing)
'U'     	universal newline mode (deprecated)'''

import csv

# f=open("d:\\python8\\james\\mystudent.csv","w") or
with open("mystudent.csv","w") as f:
    writerobj=csv.writer(f)
    writerobj.writerow(["sno","sname","scity"])


print("Data is Saved")
    

