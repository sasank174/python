
import mymodule
import pickle,time

f=open("myeinfo123","rb")

name=input("Enter ename for Search ")

while True:
    try:
        e=pickle.load(f)
    except EOFError:
        break
    else:
        if e.ename==name:
            print("Rec is Found ")
            print("Eno is : ",e.eno)
            print("Esalary is : ",e.esal)
            print("-"*30)

f.close()



        
