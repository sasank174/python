
#mydb.py
import cx_Oracle

def delete_rec(no):
    conn=cur=None
    try:
        conn=cx_Oracle.connect("scott","tiger","localhost:1521/orcl")
    except cx_Oracle.DatabaseError as e:
        print("Sorry Unable to contine ...")
        print("Reason ? ",e)
    else:
        cur=conn.cursor()
        cur.execute("DELETE FROM MYSTU WHERE sno=%d" %no)
        conn.commit()
        print(cur.rowcount," Rec are Deleted ....!!!")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

#calling
delete_rec(101)
