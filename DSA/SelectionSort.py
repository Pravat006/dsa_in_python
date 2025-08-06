# Selection Sort
# Time: O(n^2)
# Space: O(1)

C= [-3,6,8,-3,-5,8,2,1,6,9,-1]


def selection_sort(arr):
    n= len(arr)
    for i in range(n):
        min_Index= i
        for j in range(i+1, n):
            if arr[j] < arr[min_Index]:
                min_Index= j
        arr[i], arr[min_Index] = arr[min_Index], arr[i]


selection_sort(C)
print(C)




