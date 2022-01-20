import cx_Oracle
import time

conn=None
cur=None

try:
    conn=cx_Oracle.connect("scott","tiger","localhost:1521/orcl")
    
except cx_Oracle.DatabaseError as ref:
    print("Sorry Unable to continue ....")
    print("Reason is : ",ref)
    
else:
    cur=conn.cursor()
    cur.execute("SELECT * from dept")
    t=cur.fetchall()
    for row in t:
        for col in row:
            time.sleep(.1)
            print(col,end='\t\t')
        print(" ")
    
finally:
    if cur!=None:
        cur.close()

    if conn!=None:
        conn.close()
