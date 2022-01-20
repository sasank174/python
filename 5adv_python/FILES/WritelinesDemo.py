
import time

lst=["1.Rose is a nice flower \n","2.Lilly is brother of Rose \n",
        "3.Roja is sister of Lilly \n"]

f=open("flowers","w")
f.writelines(lst)
f.close()
print("Rec are saved ")
