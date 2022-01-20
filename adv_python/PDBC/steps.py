
''' Steps for PDBC

    step1: import cx_Oracle and if required any other modules
                          import cx_Oracle

   step 2: Est connection with Oracle Database by using connect() from cx_Oracle
                        connect(str,str,str) -> Connection object
                        str --> username  | scott
                        str --> password  |  tiger
                        str --> Database information
                                        ipaddress : portnumber / service id
                                        localhost: 1521 : orcl

                        To know the service id of oracle Database then we have to use
                            > Select * from global_name;


              conn=cx_Oracle.connect("scott","tiger","localhost:1521/orcl")
              if conn!=None:
                 print("Connection is Est ")
              else:
                 print("connection is Failed")

   Step-3: Create cursor object for sending the queries to the database
                  to create cursor object then we have to use cursor() from conn class
                  cursor( ) -> cursor object

                  Eg:   cur=conn.cursor()


  step-4: Sending the quires to execute @ Database by using the following
                    execute(str) From cursor class

                    Eg:  cur.execute(Query);   //Query : create | alter | delete | update | insert | select
                            cur.execute( "create table ssinfo(sno number(3),sname varchar(20)) " )



   step-5: If we execute "Select " query then result of the "Select" Query always stores
                 in the "cursor" Object

                 Inorder To Get The Records From the Cursor Object
                               then we have to use predefined methods from cursor class
                               
                                fetchone() -> tuple
                                fetchmany(int) -> list of tuples
                                fetchall()-> list of tuples

  Step-6 Based in the appcation requirements we have to process of Database Result
                        in Python

  Step-7: After All Database Operations the have to close the connection and cursor object
                         using close() from connection class
                                    close( ) from cursor class
                                           Eg:  cur.close()
                                                    conn.close()
         
 Note: After Performing Insert | update | delete operations from the PDBC then
                 we have to save the transaction by using commit() from connection class

           IF U want cancel the last transaction then we have to use
                       rollback() from connection class.
   '''






