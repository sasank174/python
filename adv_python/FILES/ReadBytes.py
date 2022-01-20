
import time

f=open("flowers","r")
data=f.read(6)
print("Data is : ",data)

data=f.read(6)
print("Data is : ",data)

pos=f.tell()
print("File Pointer @ : ",pos)

f.seek(0)
pos=f.tell()
print("File Pointer @ : ",pos)

data=f.read(5)
print("Data is : ",data)
