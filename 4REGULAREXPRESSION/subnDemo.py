
import re

data=" hello my dear friend how are you. Happy to see dear "
t=re.subn(r"\b\w{3}\b","***",data)
print("Type is : ",type(t))
print("Result is : ",t[0])
print("No.of.Replacements are : ",t[1])
