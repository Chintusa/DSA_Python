import heapq

def kth_smallest(lst, k):
    if k > len(lst) or k <= 0:
        return None
    lst=lst.copy()
    
    # Convert list into a min-heap
    heapq.heapify(lst)
    
    # Pop k-1 smallest elements
    for _ in range(k - 1):
        heapq.heappop(lst)
    
    # The next popped element is the kth smallest
    return heapq.heappop(lst)

# Example usage
arr = [7, 2, 10, 4, 3, 1]
k = 3
result = kth_smallest(arr, k)  # Use .copy() if you want to keep original list unchanged
print("Kth smallest element is:", result)  
