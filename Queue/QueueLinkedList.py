class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class QueueDoublyLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, data):
        node = Node(data)
        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            node.prev = self.rear
            self.rear = node
        self.size += 1

    def dequeue(self):
        if self.front is None:
            print("Queue is empty!")
            return None
        item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None  # Fix: reset rear if queue becomes empty
        else:
            self.front.prev = None
        self.size -= 1
        return item

    def getfront(self):
        if self.front is None:
            print("Queue is empty!")
            return None
        return self.front.data

    def display(self):
        if self.front is None:
            print("Queue is empty!")
            return
        curr = self.front
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")


q = QueueDoublyLinkedList()
q.enqueue("A")
q.enqueue("T")
q.enqueue("K")
q.enqueue("M")
q.enqueue("D")
q.enqueue("W")
q.enqueue("S")
q.display()    

print()
print(q.getfront())   # A
print(q.dequeue())    # A
print(q.dequeue())    # T
q.display()
