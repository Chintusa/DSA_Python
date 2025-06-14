from Node import Node
class SinglyCircularLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    
    def append(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
            self.tail=node
            node.next=self.head
        else:
            self.tail.next=node
            self.tail=node
            node.next=self.head
        self.size+=1
    
    def display(self):
        curr=self.head
        if  self.head is not None:
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
            self.tail.next=self.head
        else:
            node.next=self.head
            self.head=node
            self.tail.next=self.head
        self.size+=1

    def insert(self,pos,data):
        node=Node(data)
        if not(0< pos <self.size+2):
            print("Insertion not possible")
            return
        elif self.head is None:
            self.head=node
            self.tail=node
            return
        elif pos==self.size+1:
            self.append(data)
            return
        elif pos==1 :
            self.appendFirst(data)
            return

        else:
            curr=self.head
            for _ in range(1,pos-1):
                curr=curr.next
            node.next=curr.next
            curr.next=node
        self.size+=1

    def delete(self):
        if self.size==0 :
            print("Nothing to delete")
            return
        elif self.tail :
            curr=self.head
            count=1
            while curr :
                if count == (self.size-1):
                    break
                curr=curr.next
                count+=1
            curr.next=self.head
            self.tail=curr
            self.size-=1

    def deleteFirst(self):
        if self.size==0 or self.head is None :
            print("Nothing to delete")
            return
        self.head=self.head.next
        self.tail.next=self.head
        self.size-=1
    def remove(self,pos):
        count=1
        if self.size==0 :
            print("Nothing to delete")
            return
        elif(pos==1):
            self.head=self.head.next
        elif(pos==self.size):
            self.delete()

        curr=self.head
        prev=self.head
        count=1
        while curr :
            if count == pos:
                break
            prev=curr
            curr=curr.next
            count+=1
        prev.next=curr.next
        # curr.next=None
        self.size-=1
    def search(self,data):
        if self.head is None :
            print("Nothing to search")
            return
        curr=self.head
        pos=1
        while curr:
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
            










