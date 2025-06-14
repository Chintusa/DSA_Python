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
            if self.tail is None :
                self.tail=node
        else:
            self.tail.next=node
            node.prev=self.tail
            self.tail=node
        self.size+=1
    def display(self):
        curr=self.head
        while curr :
            print(curr.data,end=" -> ")
            curr=curr.next
        print("None\n")
    def get_size(self):
        return self.size
    def appendFirst(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
            if self.tail is None :
                self.tail=node
        else:
            node.next=self.head
            self.head.prev=node
            self.head=node
        self.size+=1
    def insert(self,pos,data):
        node=Node(data)
        if not(0< pos <self.size+2):
            print("Insertion not possible")
            return
        elif self.head is None:
            self.head=node
            if self.tail is None :
                self.tail=node
            return
        elif pos==1:
            self.appendFirst(data)
            return
        elif pos==self.size+1:
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
        elif self.tail :
           self.tail=self.tail.prev
           self.tail.next=None
        self.size-=1
    def deleteFirst(self):
        if self.size==0 or self.head is None :
            print("Nothing to delete")
            return
        self.head=self.head.next
        self.head.prev=None
        self.size-=1
    def remove(self,pos):
        count=1
        if self.size==0 :
            print("Nothing to delete")
            return
        elif pos <= 0 or pos > self.size:
            print("Index out of bound")
            return
        elif(pos==1):
            self.head=self.head.next
            return
        elif(pos==self.size):
            self.delete()
            return

        curr=self.head
        count=1
        while curr :
            if count == pos:
                break
            prev=curr
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



from DoublyLinkedList import DoublyLinkedList
class Test:
    def test():
        l=DoublyLinkedList()
        l.append(1)
        l.append(2)
        l.append(3)
        l.append(4)
        l.append(5)
        l.append(6)
        l.append(7)
        l.append(8)
        l.append(9)
        while True: 
            print("Enter you choice :")
            ch=int(input("1.Apend\n2.display\n3.size\n4.appendFirst\n5.insert\n6.deleteLast\n7.deleteFirst\n8.delete\n9.search\n10.insert before an element\n11.insert after an element\n12.exit\n"))
            if ch==1:
                l.append(int(input("Enter the data:")))
            elif ch==2:
                l.display()
            elif ch==3 :
                print(l.get_size())
            elif ch==4 :
                l.appendFirst(int(input("Enter the data:")))
            elif ch==5 :
                l.insert(int(input("Enter the Pos :")),int(input("Enter the data :")))
            
            elif ch==6 :
                l.delete()
            elif ch==7:
                l.deleteFirst()
            elif ch==8:
                l.remove(int(input("Enter the Pos :")))
            elif ch==9:
                pos=l.search(int(input("Enter the data :")))
                if pos == -1:
                    print("Element not found!")
                else:
                    print(pos)
                
            elif ch==10:
                 l.addBefore(int(input("Enter the element :")),int(input("Enter the new Data :")))
            elif ch==11:
                 l.addAfter(int(input("Enter the element :")),int(input("Enter the new Data :")))
            elif ch==12:
                break
            else:
                print("Invalid choice!")
    test()
            
            
            