
import zipfile,time

f=zipfile.ZipFile("data.zip","r",zipfile.ZIP_STORED)
names=f.namelist()
#namelist() from zipfile  here f is zipfile object

for name in names:
    time.sleep(1)
    print("Extracted From ZipFile : ",name)
    print("- "*30)
    print("Data From ",name)
    print(" - "*30)
    f=open(name,"r")
    data=f.read()
    time.sleep(1)
    print(data)

f.close()
