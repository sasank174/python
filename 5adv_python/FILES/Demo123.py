
Files  
   open(str filename,str filemode)  -> file object 

   File Modes :
	    "w" : write mode 
		       f=open("sample","w")

        "a" : append mode
		      f=open("sample","a")
			  
		"r" : read mode 
		     f=open("sample","r")  or
			 f=open("sample")  ---> FileNotFoundError

	    "x" : Exc.Mode
		       f=open("Sample","x") ---> FileExistsError

		"w+"  : write and Read
		"a+"   : append and Read
		"r+"   : read and Write

File Methods 
    close()
	closed --> True | False 
	readable()
	writable()

Methods For Writing Data 
   write(str)
   writelines(iterable)
               str | list | tuple | set 

For Reading
read( ) -> str
read(bytes) -> str
readline( ) -> str
readlines( ) -> list


























