def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]
def selectionSort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        swap(arr, i, min_idx)
arr = [64, 25, 12, 22, 11]
selectionSort(arr)
print("Selection Sorted:", arr)