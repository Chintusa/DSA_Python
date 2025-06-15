def swap(arr,a,b):
    arr[a],arr[b]=arr[b],arr[a]

def getPivot(arr,low,high):
    pivotEle=arr[high]
    pivotPos=low

    for i in range(low,high):
        if arr[i] < pivotEle:
            swap(arr,i,pivotPos)
            pivotPos+=1
    swap(arr,high,pivotPos)
    return pivotPos




def quickSelect(arr,k,low,high):
    if low <= high :
        pivotIdx=getPivot(arr,low,high)
       
        if pivotIdx == (k-1) :
            return arr[pivotIdx]
        elif pivotIdx < (k-1):
            return quickSelect(arr,k,pivotIdx+1,high)
        else:
            return quickSelect(arr,k,low,pivotIdx-1)

arr = [7, 10, 4, 3, 20, 15]
k = 3  # To find the 3rd smallest element
result = quickSelect(arr, k, 0, len(arr) - 1)
print(f"The {k}rd smallest element is: {result}")

