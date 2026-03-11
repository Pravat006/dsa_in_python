# 21. Selection Sort

def selectionSort(arr):
    n= len(arr)
    for i in range(n-1):
        min_idx=i
        # find the minimum from the rest of the unsorted array
        for j in range(i+1, n):
            if arr[j]< arr[min_idx]:
                 min_idx= j
        arr[i], arr[min_idx]= arr[min_idx], arr[i]

arr = [64, 25, 12, 22, 11]
print("Original array:", arr)
selectionSort(arr)
print("Sorted array:", arr)
