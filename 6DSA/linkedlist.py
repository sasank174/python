class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
	
	def reverse(self):
		p = self.head
		q=r=None
		while p:
			r,q = q,p
			p = p.next
			q.next = r
		self.head = q
	
	def append(self,value):
		t = Node(value)
		if self.head is None:
			self.head = t
			return 
		temp = self.head
		while temp.next:temp = temp.next
		temp.next = t
	
	def push(self,value):
		t = Node(value)
		t.next = self.head
		self.head = t
	
	def insertAt(self,pos,value):
		t = Node(value)
		if pos == 0:
			self.push(value)
			return 
		count = 1
		p = self.head
		q = p.next
		while count < pos:
			if q == None:
				print("invalid index")
				return 
			p = p.next
			q = p.next
			count+=1
		p.next = t
		t.next = q

	def count(self):
		count = 0
		max = min = None
		temp = self.head
		while temp:
			if max == None:max = min = temp.data
			if temp.data > max:max = temp.data
			elif temp.data < min:min = temp.data
			temp = temp.next
			count+=1
		print("count = ",count)
		if max != None:
			print("Max is: {}, Min is: {}".format(max,min))

	def printList(self):
		temp = self.head
		while temp:
			print(temp.data)
			temp = temp.next

if __name__=='__main__':
	ll = LinkedList()

	ll.append(10)
	ll.append(20)
	ll.append(30)
	ll.push(50)
	ll.insertAt(4,150)
	ll.count()


	ll.printList()