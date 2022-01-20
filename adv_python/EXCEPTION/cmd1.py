#cmd1.py   command ling arguments are treated by PVM as string
import sys

try:
    x=int(sys.argv[1])
    y=int(sys.argv[2])
    z=x/y
except IndexError:
    print("Plz Enter min 2 values ")
except ValueError:
    print("Plz Enter an int input ")
except ZeroDivisionError:
    print("Sorry V R N D By Zero...")
else:
    print("Result is : ",z)
