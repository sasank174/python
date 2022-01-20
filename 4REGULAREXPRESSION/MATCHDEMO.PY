
''' What to search is nothing but Pattern
    - we can specify the pattern by using compile()-> Pattern
       compile(str) from re module .

   Where to search is nothing but target
     - we can specify the target by using match( ) | search( ) | finall( ) from pattern class

     match() -> match or None
            if the first word of target is matched given pattern then it will return match class
            object otherwise it will return None'''



import re
p=re.compile("m\w\w")   # first letter should be small 'm' then 2nd and 3rd letters can be anything
print("Type is : ",type(p))

m=p.match("dad raj ravi manasa samatha mug jug gun mom")
print("Type is : ",type(m))
print("Match Object : ",m)






