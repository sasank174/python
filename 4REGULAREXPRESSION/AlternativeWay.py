
import re

''' App-1
p=re.compile("m\w\w")
m=p.match("mat mam dad mom james ravali map")  '''

m=re.match("m\w\w","mat mam dad mom james ravali map")
print("Match : ",m)
print("- "*50)

'''
p=re.compile("m\w\w")
m=p.sarch("mat mam dad mom james ravali map")   '''

m=re.search("m\w\w","mat mam dad mom james ravali map")
print("Match : ",m)
print("- "*50)

'''
p=re.compile("m\w\w")
lst=p.findall("mat mam dad mom james ravali map")  '''

lst=re.findall("m\w\w","mat mam dad mom james ravali map")
print("matches : ",lst)













