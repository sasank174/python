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
    cur.execute("SELECT empno,ename,job,sal from emp")
    t=cur.fetchall()
    for row in t:
        time.sleep(.5)
        print("Emp_no       : ",row[0])
        print("Ename         : ",row[1])
        print("Job              : ",row[2])
        print("Salary         : ",row[3])
        print("- "*20)
    
finally:
    if cur!=None:
        cur.close()

    if conn!=None:
        conn.close()
