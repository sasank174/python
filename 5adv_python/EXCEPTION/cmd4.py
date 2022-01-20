#cmd4.py   command ling arguments are treated by PVM as string
import sys

try:
    x=int(sys.argv[1])
    y=int(sys.argv[2])
    z=x/y
except Exception as r:
    print("Sorry Unable to continue ")
    print("Reason ? : ",r)
else:
    print("Result is : ",z)
