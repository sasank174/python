
import re
import time

citr=re.finditer("[!#$]"," Hello 5 Myd7ear 1$3 Have a 8 nice Day !@#")

for m in citr:
    time.sleep(1)
    print("Match : ",m.group()," Found @ : ",m.start())







