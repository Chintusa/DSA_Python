class MinHeap:
  def __init__(self):
    self.heap=[0] # [] for 0-based and [0] for 1-based indexing
    self.size = 0

  def _heapify_up(self, idx):# 1- based indexing nlogn
    while idx//2 > 0:
      if self.heap[idx] < self.heap[idx//2]:
        self.heap[idx],self.heap[idx//2]=self.heap[idx//2],self.heap[idx] 
      idx//=2

  def insert(self,data):
    self.heap.append(data)
    self.size += 1
    self._heapify_up(self.size) # self.size-1 for 0-based  and self.size fro 1-based indexing

  def delete_root(self):  
    return self.delete_element_at_index(1)
  
  def delete_element(self,ele):
    idx=self.heap.index(ele)
    return self.delete_element_at_index(idx)
  
  def delete_element_at_index(self,idx):
    if self.size == 0:
      return None
    item=self.heap[idx]
    self.heap[idx]=self.heap[self.size]
    self.heap.pop()
    self.size-=1
    self._heapify_down(idx)
    return item

  def _get_min_child(self, idx):
    if 2 * idx + 1 > self.size:  # only left child exists
        return 2 * idx
    if self.heap[2 * idx] < self.heap[2 * idx + 1]:
        return 2 * idx
    else:
        return 2 * idx + 1




  def _heapify_down(self,idx):
    while 2 * idx <= self.size:
      minChild = self._get_min_child(idx)
      if self.heap[idx] > self.heap[minChild]:
        self.heap[idx],self.heap[minChild]=self.heap[minChild],self.heap[idx] 
      idx=minChild
      

    
  def display(self):
    print("Heap array (1-based):", self.heap[1:])


arr=[30,25,24,23,16,15,13,12,7,5,4,3]
minh = MinHeap()
for i in arr:
  minh.insert(i)

minh.display()

  


