
#cmd3.py
import sys
import time


print("All Cmd Args : ",sys.argv)

for i in sys.argv[1::]:
    time.sleep(1)
    print(i)
