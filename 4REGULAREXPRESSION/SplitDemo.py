
import re

data=" hello my dear friend how are you. Happy to see dear "
lst=re.split("\\b\w{3}\\b",data)
print("Type is : ",type(lst))
print("Result is : ",lst)

