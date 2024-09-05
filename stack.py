class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
    def Push(self,val):
        new = Node(val) 
        new.next = self.top
        self.top = new
    def Pop(self):
        ptr = self.top 
        self.top = ptr.next
        val = ptr.data
        del ptr
        return val
    def Top(self):
        return self.top
    def display(self):
        ptr = self.top
        print("Top: -> ")
        while ptr!= None:
            print("____")
            print(ptr.data)
            ptr = ptr.next

st1 = Stack()
st1.Push(10)
st1.Push(20)
st1.Push(30)
st1.Pop()
print(st1.Top().data)
st1.Push(40)
st1.display()
