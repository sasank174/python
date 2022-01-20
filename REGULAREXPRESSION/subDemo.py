
import re

data=" hello my dear friend how are you. Happy to see dear "
s=re.sub(r"\b\w{3}\b","***",data)
print("Type is : ",type(s))
print("Result is : ",s)
