#cmd2.py   command ling arguments are treated by PVM as string
import sys

try:
    x=int(sys.argv[1])
    y=int(sys.argv[2])
    z=x/y
except (ZeroDivisionError,ValueError,IndexError) as ref:
    print("Sorry Unable to continue ....")
    print("Reason is ? : ",ref)
else:
    print("Result is : ",z)
