# 19. Binary Search (Sorted Array)
'''
Given a sorted array of integers and a target value, write a program to determine if the target exists in the array using binary search. If found, print "Found"; otherwise, print "Not Found".

'''


def binSearch(arr, target):
    if not len(arr):
        return "Not Found"
    left= 0
    right= len(arr)-1

    while left<=right:
        mid= (left+right)//2

        if arr[mid]==target:
            return "Found"
        elif target< arr[mid]:
            right= mid-1
        else:
            left = mid+1
    return "Not Found"

print(binSearch([2,3,4,5,6], 5))


