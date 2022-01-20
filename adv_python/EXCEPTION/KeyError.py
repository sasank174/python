
stu={"sno":101,"sname":"ramesh","scity":"hyd"}
print(stu)

key=input("Enter Key : ")  #sname

if key in stu.keys():
    value=stu[key]
    print("Value For Key is : ",value)
else:
    print("Sorry Key is Not Existed ")
