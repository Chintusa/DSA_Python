class Queue:
    def __init__(self,capacity):
        self.capacity=capacity
        self.queue=[]
        self.size=0
    def enqueue(self,data):
        if self.size == self.capacity :
            print("Queue is full! No more Insertion is possible.")
            return
        self.queue.append(data)
        self.size+=1
    def dequeue(self):
        if self.size == 0 :
            print("Queue is empty!No more deletion is possible.")
            return
        self.size-=1
        return self.queue.pop(0)
    def display(self):
        if self.size ==0 :
            print("Queue is empty!")
            return
        print(self.queue)
    def front(self):
        if self.size ==0 :
            print("Queue is empty!")
            return
        return self.queue[0]
   

q = Queue(3)
q.enqueue("A")
q.enqueue("T")
q.enqueue("K")
q.enqueue("M")
print(q.dequeue())
print(q.dequeue())
q.enqueue("D")
q.enqueue("W")
q.enqueue("S")
print(q.front())


q.display()    
