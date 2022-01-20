
''' exists(path) from os.path module
    it will return True if specified path is existed else return False

    isFile(path) from os.path module
    it will returns True if specified path is a File else return False

    isdir(path) from os.path module
    it will returns True if the specified path is a directory else return False'''

import os.path

if os.path.exists("d:\\python8\\lambda\\EX1.py"):
    print("Path is existed ")
    if os.path.isfile("d:\python8\lambda\ex1.py"):   
        print("Path is a File ")
    else:
        print("Path is a directory")    
else:
    print("Sorry Given path is not existed ")
    

