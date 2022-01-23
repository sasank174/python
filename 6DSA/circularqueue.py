class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = self.last = None
    
    def enqueue(self,value):
        t = Node(value)
        temp = self.head
        t.next = self.head
        if self.head == None:
            t.next = t
            self.head =self.last = t
            return 
        if self.head == self.last:
            self.head.next = t
            self.last = t
        else:
            self.last.next = t
            self.last = t
    
    def dequeue(self):
        if self.head == None:
            print("queue is empty")
            return 
        if self.head == self.last:
            print("--> " + str(self.head.data))
            self.head = self.last = None
            return 
        print("--> " + str(self.head.data))
        self.head = self.head.next
        self.last.next = self.head

    def display(self):
        if self.head ==None:print("nothing to display")
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
            if temp == self.head:
                break



if __name__ == "__main__":
    q = Queue()

    q.enqueue(1)
    q.enqueue(2)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.enqueue(3)
    q.enqueue(3)
    q.enqueue(3)
    q.enqueue(5)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()

    q.display()