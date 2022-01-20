
import mymodule
import pickle,time

with open("myeinfo123","rb") as f:
    while True:
        time.sleep(1)
        try:
            e=pickle.load(f)            
        except EOFError:
            break
        else:
            if isinstance(e,mymodule.Employee):
                e.getEmployee()
            else:
                pass
            print("- "*20)
    
          
