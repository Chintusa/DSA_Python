class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
        self.prev=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def append(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
            self.tail=node
        else:
            node.prev=self.tail
            self.tail.next=node
            self.tail=node
    def insert(self,data,pos):
        
            
