lis = [1,2,"asa",1.3,10]
print(lis)
print(type(lis))

lis = list((1,2,"asa",1.3,10))

lis[2] = "sasank"
print(lis)
print(lis[2])
print(lis[2:])
print(len(lis))
print("sasank" in lis)

lis.append("appended")
lis.insert(1,"insert")
lis.extend(lis)
lis2 = lis+lis


lis.remove("appended")  # error if not exist
lis.pop()

lis.reverse()

lis2 = lis.count(10)
lis2 = lis.copy()
print(lis2)

