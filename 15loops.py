i = 1
while i < 10:
    print(i)
    i += 1

i = 1
while i < 5:
    print(i)
    if i == 3:break
    i += 1


while i < 5:
    i += 1
    if i == 3:continue
    print(i)

i=0
while i < 5:
    print(i)
    i += 1
else:
    print("while loop ended")

# ========================================================================================================================



l = ["sa", "sas", "sasank"]
for x in l:
    print(x)

for x in "sasank":
    print(x)

for x in l:
    if x == "sas":break
    print(x)

for x in l:
    if x == "sas":continue
    print(x)

for x in range(0,5):
    print(x)

for x in range(0,5):
    print(x)
else:
    print("for loop ended")

for x in range(0,5):
    print(x)
    if x == 2:break
else:
    print("for loop ended")  # if loop breaks else is also not executed