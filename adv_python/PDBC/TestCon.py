
''' Program to intract to with oracle Database '''

import cx_Oracle

conn=cx_Oracle.connect("scott","tiger","localhost:1521/orcl")

if conn!=None:
    print("Connection is Est ")
else:
    print("Sorry Connection is Fail")

conn.close()

