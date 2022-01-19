s = {1,2,"asa",1.3,10,10}
print(s)
print(type(s))

print(len(s))

s.add("sasank")
s.update(["ha","ha1"])

s.remove("ha") # will raise error
s.discard("ha") # no error
s.pop("ha")

print(*s,sep=",")
print("asa" in s)

# ==============================


a = set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set1.update(set2)
print(set1)

set1.intersection_update(set2)
set4 = set1.intersection(set2)


set1.symmetric_difference_update(set2)
set5 = set1.symmetric_difference(set2)