
stu={"sno":101,"sname":"ramesh","scity":"hyd"}
print(stu)

key=input("Enter Key : ")  #sname
try:
    value=stu[key]
    print("Value For Key is : ",value)
except KeyError:
    print("Sorry Key Is Not Existed ")



