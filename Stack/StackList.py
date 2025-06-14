class Stack:
    def __init__(self,capacity):
        self.stack=[]
        self.capacity=capacity
        self.top=-1
    def push(self,data):
        if self.top+1 == self.capacity:
            print("Stack overflow! insertion not possible.")
            return
        self.top+=1
        self.stack.append(data)
    def pop(self):
        if self.top == -1:
            print("Stack underflow! No more Deletion possible.")
            return
        self.top-=1
        return self.stack.pop()
    def peek(self):
        if self.top == -1:
            print("Stack underflow!")
            return
        return self.stack[self.top]
    def size(self):
        return self.top+1
    def display(self):
        print(self.stack[:self.top+1])



        
s=Stack(3)
s.push("A")
print("Peek :",s.peek())
s.display()
s.push("T")
print("Peek :",s.peek())
s.display()
s.push("k")
print("Peek :",s.peek())
s.display()
s.push("M")
print("Peek :",s.peek())
s.pop()
s.pop()
s.display()
s.push("D")
print("Peek :",s.peek())
s.push("W")
print("Peek :",s.peek())
s.push("S")
print("Peek :",s.peek())
s.display()




