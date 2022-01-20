a = 10
b = 100
c = 1000

if b > a:
    print("b is greater than a")

if b > a:
    print("b is greater than a")
else:
    print("a is greater than b")


if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

if a > b and c > a:print("Both conditions are True")
if a > b or c > a:print("Both conditions are True")

# shorthand

if a > b: print("a is greater than b")
print("A") if a > b else print("B")

