# * U Must Install Oracle 11.2 and higher version
#        Username : scott
# 	   password : tiger 

# DEFAULT user in Oracle
#     Username : system
# 	password : manager

# Oracle Basic Command:
#    Create 
#       Syn: SQL>create  <table>  <tablename>
# 	                     (<column_name>     <datatype>(size), ........ , <Column_n>);

# 	Eg:  SQL>create table student
# 	                  (sno  number(3),sname varchar(20),scity varchar(20));

#   2.sql>show user 
#           - it will display the current username

#   3.SQL>Select * from tab;
#         - It will shows u all objects [tables] existed in the current user

#   4. To see table description of the table 
#          Column names |  data types and | size of the column ....
# 		 SQL>Desc  <tablename>;

		
#  5.Insert 
#      Syn:SQL>INSERT INTO <tablename>
# 	                   (<column1>,<column2>,......,<column n>)
# 					   VALUES					  
# 					   (<value1>,<value2>,......,<valuen>);

# SQL> INSERT INTO STUDENT
#   2  (SNO,SCITY)
#   3  VALUES
#   4  (101,'KMM');

# SQL> INSERT INTO STUDENT
#   2  VALUES
#   3  (102,'LILLY','UK');

# ALTER
# SQL>ALTER <table> <tablename>
#           ADD | Modify | Drop
# 		  (<Column>   <datatype>(size) );

# SQL> ALTER TABLE STUDENT
#   2  ADD
#   3  (FNAME VARCHAR(20));

# SQL> ALTER TABLE STUDENT
#   2  DROP COLUMN SCITY;

# SQL> alter table student
#   2  modify
#   3  (fname CHAR(10));

# SQL> ALTER TABLE STUDENT
#   2  RENAME COLUMN
#   3  SNAME TO STU_NAME;

#  To Read the Data From the Table Then we have to user 
#  SELECT 

#  SQL>SELECT <COLUMNList> From <tablename>
#            [WHERE <condition>];

# Eg: SQL>Select empno from emp;
# SQL>Select empno,ename,job from emp;
# SQL>Select * from emp;

# Based On Some Condition Then We Have to Use [Where <condition>]
# sql>select ename,job,sal
#         FROM emp where job='MANAGER';

# sql>Select * from emp
#        where hiredate>='19-APR-87';

# SQL>SELECT * from emp where sal<3000;
# SQL>Select * from emp where comm is null;

# Sorting records while Reading Data From table   Then We have to Order by
# SQL>SELECT <columnList>
#           From  <tablename>
# 		  [Where <condition>]
# 		  [Order by <column> [desc] ];

# Eg: SQL>select ename from emp order by ename;
#        SQL>select ename from emp order by ename desc;
# 	   sql>SELECT ename,job,sal from emp order by sal desc;
# 	   SQL>Select * from emp order by hiredate;

# UPDATE:
#    It is used to make the changes in the data which is already existed .

#   Syn: SQL>UPDATE <TABLENAME>
#                      SET <COLUMN>=<VALUE>,.........
# 					 [WHERE <CONDITION>];

# Eg: SQL>update emp SET sal=9000;
#         SQL>update emp SET sal=7000,comm=333 where JOB='MANAGER';
# 		sql>UPDATE EMP SET SAL=SAL+(SAL*10)/100,
# 		                                          COMM=COMM+(COMM*5)/100
# 												  WHERE job='CLERK';

# DELETE:
#    SQL>DELETE FROM <TABLEAME>
#              [WHERE <CONDITION>];

#    sql>DELETE FROM EMP WHERE JOB='clerk';
#    sql>delete from emp where job='MANAGER';
#    SQL>DELETE FROM EMP;

# To Create duplicat table :
#   SQL>Create table tablename
#   as
#   select * from tablename;

# If u want cancel the last operation [ DELETE | INSERT | UPDATE]
#                                                                           then we have to use 
# sql>ROLLBACK

# sql>commit
#    To make the operations saved 
#    After Insert | update | delete u better use commit
#    Once the records are commited then rollback doesn't work on it.

# ICURD







































































