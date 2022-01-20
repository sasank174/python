
''' program to Insert group of  records into table mystu
    Insert into mystu values(val1,val2,val3,.....)'''

import cx_Oracle
conn=cur=None

try:
    conn=cx_Oracle.connect("scott","tiger","localhost:1521/orcl")

except cx_Oracle.DatabaseError as r:
    print("Sorry unable to connect")
    print("Reason ? : ",r)

else:
    cur=conn.cursor()
    query=" INSERT INTO MYSTU VALUES(%d,'%s','%s') "
    while True:
        sno=int(input("Enter sno : "))
        sname=input("Enter sname : ")
        scity=input("Enter scity : ")
        cur.execute(query %(sno,sname,scity))
        opt=input("Do u want another rec y|n")
        if opt in['N','n']:
            conn.commit()
            break            
        
finally:
    if cur!=None:
        cur.close()
        
    if conn!=None:
        conn.close()
        


















