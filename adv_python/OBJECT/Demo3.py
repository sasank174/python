class Employee:
    ''' This is For Employee  Salary Information System '''
    def __init__(self):
        self.eno=101
        self.ename="Ramesh"


#calling
print(dir(object))
print("= "*30)

e=Employee()
print("Docstring of Employee : ",e.__doc__)
print("Class Name of of e object : ",e.__class__)
print("Module Name is : ",e.__module__)

print("Attributes and Their value : ",e.__dict__)

'''Adding an instance field to an object from outside of the class  '''
#e.ejob='Manager'   
e.__setattr__('ejob','MANAGER')
print("After Adding : ",e.__dict__)
print(" - "*30)

''' Reading the value of an attribute from outside of the class '''
#name=e.ename
name=e.__getattribute__('ename')
print("Ename is : ",name)
print(" - "*30)

'''Deleting attributes from the object from outside of the class '''
#del e.eno
e.__delattr__('eno')
e.__delattr__('ename')
print("After deleting an attribute ",e.__dict__)
       






