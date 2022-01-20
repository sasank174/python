#cmd3.py   command ling arguments are treated by PVM as string
import sys

try:
    x=int(sys.argv[1])
    y=int(sys.argv[2])
    z=x/y
except:
    print("Sorry Unable to continue ")
else:
    print("Result is : ",z)
