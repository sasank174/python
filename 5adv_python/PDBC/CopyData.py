
''' Reading Data From emp and stores them into employee.csv '''

import cx_Oracle
import csv
import time

conn=None
cur=None
f=None

try:
   conn=cx_Oracle.connect("scott","tiger","localhost:1521/orcl")
except cx_Oracle.DatabaseError as r:
    print("Sorry Unable to continue ...")
    print("Reason : ",r)
else:
    cur=conn.cursor()
    cur.execute("select ename,job,sal from emp")

    f=open("employee.csv","w",newline='')
    csvwriter=csv.writer(f)

    for t in cur:
        time.sleep(.1)
        csvwriter.writerow(t)

    time.sleep(1)
    print("Records are copied ")
    
finally:
    if f!=None:
        f.close()

    if cur!=None:
        cur.close()

    if conn:                
        conn.close()



