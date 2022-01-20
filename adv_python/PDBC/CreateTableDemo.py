
''' program to create a table in oracle database '''

import cx_Oracle

conn=None
cur=None

try:
    conn=cx_Oracle.connect("scott","tiger","localhost:1521/orcl")
    
except cx_Oracle.DatabaseError as r:
    print("Sorry Unable to continue ...")
    print("Reason  ? : ",r)

else:
    print("Connection is Est ")
    cur=conn.cursor()
    cur.execute(" CREATE TABLE MYSTU(SNO NUMBER(3),SNAME VARCHAR(10),SCITY VARCHAR(10)) ")
    print("Table is Created in Oracle Database ....!!!")

finally:
    if cur!=None:
        cur.close()
        
    if conn!=None:        
        conn.close()
    



