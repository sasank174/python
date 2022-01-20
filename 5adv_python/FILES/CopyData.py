import time

fsrc=None
ftrg=None

try:
    sfile=input("Enter src_file name : ")
    fsrc=open(sfile,"r")
except FileNotFoundError:
    print("Sorry SRC File Is Not Found ")    
else:
    tfile=input("Enter trg_file name : ")
    try:
        ftrg=open(tfile,"x")
    except FileExistsError:
        print("Sorry trg_File is already Existed ...!!!")
    else:
       time.sleep(1)
       print("Data is coping....!")
       data=fsrc.read()
       ftrg.write(data)
       time.sleep(1)
       print("Data is Copied ....!")
finally:
    if fsrc!=None:
        fsrc.close()

    if ftrg!=None:
        ftrg.close()

    
