
''' program to Insert a record into table mystu
    Insert into mystu values(val1,val2,val3,.....)'''

import cx_Oracle

conn=cur=None
try:
    conn=cx_Oracle.connect("scott","tiger","localhost:1521/orcl")

except cx_Oracle.DatabaseError as r:
    print("Sorry Unable to continue ...")
    print("Reason is : ",r)

else:
    cur=conn.cursor()
    cur.execute("INSERT INTO MYSTU VALUES(101,'RAMESH','HYD') ")
    conn.commit()
    print("Rec is inserted ...!!!")

finally:
    if cur!=None:
        cur.close()
        
    if conn!=None:
        conn.close()


