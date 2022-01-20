
import re
import time

'''
lst=re.findall("\d","Sh&as&hi K7UM4ar 123 !@#")
print("All digits : ",lst)  '''


citr=re.finditer(".","Sh&as&hi K7UM4ar 123 !@#")

for m in citr:
    time.sleep(.5)
    print("Match : ",m.group())
    print("Found @ : ",m.start())
    print("- "*30)










