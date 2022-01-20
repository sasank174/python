
import zipfile,time

f=zipfile.ZipFile("data.zip","w",zipfile.ZIP_DEFLATED)
f.write("data1")
f.write("data2")
f.write("data3")
f.write("data4")
f.close()
time.sleep(1)
print("Files are Zipped to Stored in File name data.zip")
