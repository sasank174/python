x = "sasank"
print(x)


x = """
ansdas
ad
ad
as
d
asd
a
dasakbdkada
"""
print(x)



x = "sasank"
print(x[1])


for i in x:print(i,end=" ")
print()

print("sa" in x)

print(len(x))
print(x[:2])
print(x[-4:-1])


print(x.upper())
print(x.lower())
print(x.capitalize())
print()

print(x.strip())
print(x.replace("s","a"))
print()

print(x.split(" "))
print("".join(x))
print()


print(x+x)
print("he is {}".format(x))


x = "sasank \"is\""
print(x)