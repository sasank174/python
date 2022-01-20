#       0   1    2    3   4   5
lst=[10,20,30,40,50,60]

print("List Collection ",lst)
pos=int(input("Enter index pos : "))

if pos<len(lst):
    item=lst[pos]
    print("Item is : ",item)
else:
    print("Sorry Invalid Index ")
