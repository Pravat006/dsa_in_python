'''
45. Find Intersection of Two Arrays
Print all elements common to both arrays (in order of first array).
Assume no duplicates in either array.

Input:
Array1: 3 → 1 2 3
Array2: 3 → 2 3 4
Output: 2 3
'''

# Time: O(n*n)
arr1= [1,2,3,5]
arr2=[2,3,4,5]

for i in range(len(arr1)):
    for j in range(len(arr2)):
        if arr1[i]== arr2[j]:
            print("Common found   : ", arr1[i])
