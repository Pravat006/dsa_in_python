#27. Merge Two Arrays
'''
Takes two arrays as input and combines them into a single array by appending all elements of the second array after the first. The merged result is printed in order.

Example: [1, 2, 3] + [4, 5] → 1 2 3 4 5
'''

def mergeArr(arr1, arr2):
    # base case
    if len(arr1)==0:
        return arr2
    elif len(arr2)==0:
        return arr1
    elif len(arr1)==0 and len(arr2)==0:
        return []
    merged = [item for arr in [arr1, arr2] for item in arr]
    return merged
a= [4,5,6]
b=[7,8,9]
print(mergeArr(a,b))
