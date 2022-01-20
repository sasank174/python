
import re

p=re.compile("m\w\w")
lst=p.findall("dad mam jug cnu anu sri mad map mub sru")
print("Matches are : ",lst)
