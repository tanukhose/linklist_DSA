class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        
    def Enq(self,data):
        new = Node(data) 
        if(self.front==None):
            self.front = new
            self.rear = new
        else:
            self.rear.next = new
            self.rear = new
    def Deq(self):
        if self.front == None:
            print("Queue is Empty")
        ptr = self.front
        self.front = ptr.next
        del ptr
    def display(self):
        ptr = self.front
        while ptr!=None:
            print(ptr.data,end = "-->>")
            ptr=ptr.next
        print()

q = Queue()
# print(q.front)
# print(q.rear)
q.Enq(6)
q.Enq(7)
q.Deq()
q.Enq(8)
q.Deq()
q.Enq(19)
q.display()
print(q.rear.data)
            
















