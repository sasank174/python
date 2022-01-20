import zipfile

f=zipfile.ZipFile("test.zip","w",zipfile.ZIP_DEFLATED)
f.write("data1")
f.write("data2")
f.write("data3")
f.write("data4")
f.close()
print("File are zipped")

