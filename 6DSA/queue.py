class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = self.last = None
    
    def enqueue(self,value):
        t = Node(value)
        if self.head == None:
            self.head =self.last = t
            return 
        self.last.next = t
        self.last = t
        
    
    def dequeue(self):
        if self.head == None:
            print("queue is empty")
            return 
        self.head = self.head.next

    def display(self):
        if self.head ==None:print("nothing to display")
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next



if __name__ == "__main__":
    q = Queue()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()

    q.display()