
import re
import time

citr=re.finditer("a*"," abaabaaabaaaab")

for m in citr:
    time.sleep(1)
    print("Match : ",m.group()," Found @ : ",m.start())







