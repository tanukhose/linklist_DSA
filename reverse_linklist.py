class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        ptr = self.head
        while ptr:
            print(ptr.data, end=" -> ")
            ptr = ptr.next
        print()

    def reverse(self):
        pr = None
        new = self.head
        while new:
            next_node = new.next
            new.next = pr
            pr = new
            new = next_node
        self.head = pr

LL1 = LinkedList()

LL1.insert(10)
LL1.insert(12)
LL1.insert(16)
LL1.insert(7)
LL1.insert(9)

LL1.display()
LL1.reverse()
LL1.display()
