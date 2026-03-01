# 18. Linear Search
# 18. Linear Search

def lnrSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i 
    return -1 

arr = [10, 20, 30, 40, 50]
target = 30

result = lnrSearch(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found")