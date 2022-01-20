
import re
import time

citr=re.finditer("m\w\w","mom dad cnu anu ravi map mad mug jug")
print("Type is : ",type(citr))

'''note: callable_iterator is the collection of the match objects'''

for m in citr:
    time.sleep(1)
    #print(m)
    print("Match is : ",m.group())
    print("Starting index pos of match : ",m.start())
    print("- "*40)












