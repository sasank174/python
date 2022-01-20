
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
    query="UPDATE EMP SET SAL=SAL+%d where job='%s' "
    increment_salary=int(input("Enter Increment Amount : ")) #2000
    job_title=input("Enter Job_Title For update : ") # MANAGER
    cur.execute(query %(increment_salary,job_title) )
    conn.commit()
    print("Rec are updated....!!!")
    
finally:
    if cur!=None:
        cur.close()

    if conn!=None:
        conn.close()
