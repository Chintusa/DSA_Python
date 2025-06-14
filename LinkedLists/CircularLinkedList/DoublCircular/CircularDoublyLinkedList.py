from Node import Node
class CircularDoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def append(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
            self.tail=node
            node.prev=node
            node.next=node
        else:
            self.tail.next=node
            node.prev=self.tail
            self.tail=node
            self.tail.next=self.head
        self.size+=1

    def display(self):
        curr=self.head
        if self.head is not None :
            while True :
                print(curr.data,end=" -> ")
                curr=curr.next
                if(curr==self.head):
                    break
            print("None\n")
    
    def get_size(self):
        return self.size
    
    def appendFirst(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
            self.tail=node
            node.prev=node
            node.next=node
        else:
            node.next=self.head
            self.head.prev=node
            self.head=node
            self.head.prev=self.tail
            self.tail.next=self.head
        self.size+=1
    
    def insert(self,pos,data):
        node=Node(data)
        if not(0< pos <self.size+2):
            print("Insertion not possible")
            return
        if self.head is None:
            self.head=node
            self.tail=node
            node.prev=node
            node.next=node
            return
        if pos==1:
            self.appendFirst(data)
            return
        if pos==self.size+1:
            self.append(data)
            return
        else:
            curr=self.head
            for _ in range(1,pos-1):
                curr=curr.next
            node.next=curr.next
            node.next.prev=node
            node.prev=curr
            curr.next=node
        self.size+=1
        
    def delete(self):
        if self.size==0 :
            print("Nothing to delete")
            return
        else:
           self.tail=self.tail.prev
           self.tail.next=self.head
           self.head.prev=self.tail
        self.size-=1

    def deleteFirst(self):
        if self.size==0 or self.head is None :
            print("Nothing to delete")
            return
        else:
            self.head=self.head.next
            self.head.prev=self.tail
            self.tail.next=self.head
        self.size-=1

    def remove(self,pos):
        count=1
        if self.size==0 :
            print("Nothing to delete")
            return
        if pos <= 0 or pos > self.size:
            print("Index out of bound")
            return
        if(pos==1):
            self.head=self.head.next
            return
        if(pos==self.size):
            self.delete()
            return

        curr=self.head
        count=1
        while True :
            if count == pos:
                break
            curr=curr.next
            count+=1
        curr.prev.next=curr.next
        curr.next.prev=curr.prev
        # curr.next=None
        self.size-=1

    def search(self,data):
        if self.head is None :
            print("Nothing to search")
            return
        curr=self.head
        pos=1
        while True:
            if curr.data == data :
                return pos
            curr=curr.next
            pos+=1
        return -1

    def addBefore(self,data,newData):
        pos=self.search(data)
        if pos != -1:
            self.insert(pos,newData)
            return
        else:
            print("Element not found!")
            return

    def addAfter(self,data,newData):
        pos=self.search(data)
        if pos != -1:
            self.insert(pos+1,newData)
            return
        else:
            print("Element not found!")
            return
            