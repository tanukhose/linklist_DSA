class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            ptr = self.head
            while ptr.next != None:
                ptr = ptr.next
            ptr.next = Node(data)

    def insertpos(self, data):
        pos = int(input("Enter position: "))
        new_node = Node(data)
        ptr = self.head
        while pos > 2 and ptr != None:
            ptr = ptr.next
            pos -= 1
        new_node.next = ptr.next
        ptr.next = new_node

    def display(self):
        ptr = self.head
        while ptr:
            print(ptr.data, end=" ")
            ptr = ptr.next
        print()

LL1 = LinkedList()

LL1.insert(10)
LL1.insert(12)
LL1.insert(16)
LL1.insert(7)
LL1.insert(9)
LL1.insertpos(5)
LL1.display()