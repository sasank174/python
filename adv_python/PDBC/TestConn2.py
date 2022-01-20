
import cx_Oracle

conn=None

try:
    conn=cx_Oracle.connect("scott","tiger","localhost:1521/orcl")

except cx_Oracle.DatabaseError as r:
    print("Sorry Unable to Connect with DB ")
    print("Reason ? : ",r)

else:
    print("Connection is Est ")

finally:
    if conn!=None:
        conn.close()
        print("connection is Closed !!! ")
