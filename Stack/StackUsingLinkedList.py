class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class StackUsingLinkedList:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if self.top is None:
            print("No more elements to pop!")
            return
        item = self.top.data
        self.top = self.top.next
        self.size -= 1
        return item

    def peek(self):
        if self.top is None:
            print("No more elements to peek!")
            return
        return self.top.data

    def getSize(self):
        return self.size

    def display(self):
        if self.top is None:
            print("No elements in the stack.")
            return
        curr = self.top
        while curr:
            print(curr.data)
            curr = curr.next



s = StackUsingLinkedList()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)

print("Peek:", s.peek())  # Should print 5
print("Pop:", s.pop())    # Removes 5
s.display()               # Should print 4, 3, 2, 1

print("Pop:", s.pop())    # Removes 4
s.display()               # Should print 3, 2, 1
