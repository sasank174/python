x = "sa"
print(type(x))
print(x)
print("==========")

x = 1
print(type(x))
print(x)
print("==========")

x = 1.1
print(type(x))
print(x)
print("==========")

x = complex(1j)
print(type(x)) 
print(x.real)
print(x.imag)

print("==========================================")


x = [1,1.2,"sasa"]
print(type(x))
print(x)
print("==========")

x = (1,1.2,"sasa")
print(type(x))
print(x)
print("==========")

x = range(10)
print(type(x))
print(x)

print("==========================================")


x = {1,1.2,"sasa"}
print(type(x))
print(x)
print("==========")


x = frozenset((1,1.2,"sasa"))
print(type(x))
print(x)

print("==========================================")


x = {"1":1,"1.2":1.2,"sasa":"sasnk"}
print(type(x))
print(x)

print("==========================================")


x = True
print(type(x))
print(x)


print("==========================================")


x = b"Hello"
print(type(x))
print(x)
print("==========")

x = bytearray(5)
print(type(x))
print(x)
print("==========")

x = memoryview(bytes(5))
print(type(x))
print(x)


print("==========================================")

x = 200.0
print(isinstance(x, int)) # false