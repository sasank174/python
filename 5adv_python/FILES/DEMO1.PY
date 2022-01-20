
f=open("sample","w+")

print("Is File Writable ? : ",f.writable() )
print("Is File Readable ? : ",f.readable())
print("Is File Closed ? : ",f.closed)

f.close()
print("Is File Closed ? : ",f.closed)
