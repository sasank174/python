
import mymodule
import pickle,time

with open("myeinfo123","wb") as f:
    while True:
        e=mymodule.Employee()
        e.setEmployee()
        pickle.dump(e,f)
        opt=input("Do u want another Y|N : ")
        if opt in ['N','n']:
            break

time.sleep(1)
print("Objects are Saved ")
        
        
