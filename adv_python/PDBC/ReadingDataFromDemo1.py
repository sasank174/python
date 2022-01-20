import cx_Oracle

conn=None
cur=None

try:
    conn=cx_Oracle.connect("scott","tiger","localhost:1521/orcl")
    
except cx_Oracle.DatabaseError as ref:
    print("Sorry Unable to continue ....")
    print("Reason is : ",ref)
    
else:
    cur=conn.cursor()
    cur.execute("SELECT * FROM MYSTU")
    t=cur.fetchone()
    print(t)

    
finally:
    if cur!=None:
        cur.close()

    if conn!=None:
        conn.close()
