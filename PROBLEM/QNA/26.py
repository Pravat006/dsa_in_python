#26. Check if Array is Sorted

def isSorted(arr):
    n= len(arr)
    isSorted=True
    if not len(arr):
        return "Empty"
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            isSorted=False
            break
    return isSorted
    
    

nums=[2,5,6,8]
print(isSorted(nums))
        
