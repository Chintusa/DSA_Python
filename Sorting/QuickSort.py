def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i > j:
            break
        swap(arr, i, j)
    
    swap(arr, low, j)
    return j

def quickSort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quickSort(arr, low, p - 1)
        quickSort(arr, p + 1, high)
        

arr = [64, 25, 12, 22, 11]
quickSort(arr, 0, len(arr)-1)
print("Quick Sorted:", arr)

