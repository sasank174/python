
import sys

lst=[i for i in range(1,1001) ]
nblist=sys.getsizeof(lst)
print("Size for list Collection : ",nblist)
print("First object : ",lst[0])
print("Last object : ",lst[-1])

g=(i for i in range(1,1001) )
nbg=sys.getsizeof(g)
print("Size for Gen Collection : ",nbg)
print("First Object : ",g[0])


