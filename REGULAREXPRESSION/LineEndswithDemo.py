
import re
import time

match=re.search("d\w\wr$","have a nice day my Dear",re.IGNORECASE)

if match is not None:
    print("Line is ends with given pattern ")
else:
    print("Line is not ends with given pattern")








