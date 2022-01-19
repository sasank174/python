thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)
print(type(thisdict))
print(len(thisdict))


print(thisdict["brand"])
x = thisdict.keys()
thisdict["color"] = "white"
x = thisdict.values()
x = thisdict.items()

thisdict.update({"year": 2020})

thisdict.pop("model")
thisdict.popitem()
del thisdict["model"]
del thisdict
thisdict.clear()


mydict = thisdict.copy()
mydict = dict(thisdict)




for x in thisdict:print(thisdict[x])

for x in thisdict.values():print(x)

for x in thisdict.keys():print(x)

for x, y in thisdict.items():print(x, y)


