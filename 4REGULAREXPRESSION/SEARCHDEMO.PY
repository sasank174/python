
''' search() from pattern class
       it will ensure is there any matches are existed in the target
       if any matches are existed it will extract the only first match
       from the target and it will return in the form Match Object.
       - if none of the match existed then it will return None

      start() | end( ) | group( ) -> str all methods from Match class'''

import re

p=re.compile("m\w\w")
m=p.search("dad mom mad jug gun map mug")
print("Match is : ",m)
print("Matched String : ",m.group())
print("Starting Index Pos Of Match : ",m.start())
print("Ending Index pos+1 Of Match : ",m.end())
