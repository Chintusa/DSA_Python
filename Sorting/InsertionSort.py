def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
arr = [64, 25, 12, 22, 11]
insertionSort(arr)
print("Insertion Sorted:", arr)
