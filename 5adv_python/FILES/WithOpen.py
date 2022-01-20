import time

with open("flowers","r") as f:     # f=open("flowers","r")
    time.sleep(1)
    print("Now V R In with Block ")
    time.sleep(1)
    print("Is File closed ? : ",f.closed)

time.sleep(1)
print("Outside of with block")
time.sleep(1)
print("Is File Closed ? : ",f.closed)
