import time
f=open("data4","w")

print("Enter U R Data Press * For Exit ")
data=input()   #chinni

while data!='*':
    f.write(data+"\n")
    data=input()  #*

time.sleep(1)
f.close()
print("File is Created ")
