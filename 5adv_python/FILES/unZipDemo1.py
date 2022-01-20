import zipfile
import time

f=zipfile.ZipFile("test.zip","r",zipfile.ZIP_STORED)
names=f.namelist()
print(type(names))

for name in names:
    time.sleep(1)
    print("Filename is : ",name)

