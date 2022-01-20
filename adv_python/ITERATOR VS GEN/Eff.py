
import timeit

def fun_list():
    x=[i for i in range(1,1000)]

def fun_gen():
    x=(i for i in range(1,1000))

tflst=timeit.timeit(fun_list,number=100000)
tfgen=timeit.timeit(fun_gen,number=100000)

print("Time Taken For List Collections : ",tflst)
print("Time Taken For gen Collections : ",tfgen)

    

    
