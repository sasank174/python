class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Slinkedlist:
    def __init__(self):
        self.head = None
    
    def insert(self,value):
        t = Node(value)
        if self.head == None:
            self.head = t
            return 
        if value < self.head.data:
            t.next = self.head
            self.head = t
            return 
        
        temp = self.head
        while temp.next:
            if temp.next.data >= value:
                t.next,temp.next = temp.next,t
                break
            else:temp = temp.next
        else:temp.next = t
                
    def reverse(self):
        p = self.head
        q=r=None
        while p:
            r,q = q,p
            p = p.next
            q.next = r
        self.head = q
    
    def delete(self,value):
        temp = self.head
        if self.head.data == value:
            self.head = self.head.next
            print("deleted " + str(value))
            return 
        while temp.next:
            if temp.next.data == value:
                temp.next = temp.next.next
                print("deleted " + str(value))
                return 
            else:
                temp = temp.next
        print(str(value) +" element not found")


    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

if __name__ == "__main__":
    sl = Slinkedlist()
    sl.insert(90)
    sl.insert(10)
    sl.insert(1)
    sl.insert(50)
    sl.insert(80)
    sl.insert(70)
    sl.delete(95)
    sl.printlist()
