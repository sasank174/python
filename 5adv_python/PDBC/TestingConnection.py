
import cx_Oracle

conn=cx_Oracle.connect("sott","tiger","localhost:1521/orcl")

if conn!=None:
    print("Connection is Est  ...  :)   ")
else:
    print("Sorry Connection is Gone....!")
