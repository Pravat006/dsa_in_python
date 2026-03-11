'''
37. Find Minimum Element in Array
Traverse the array and track the smallest value encountered.

Input: 5 → 3 1 4 1 5
Output: 1

'''

def smallest(nums):
    if len(nums)==0:
        return "Empty array"
    elif len(nums)==1:
        return nums[0]
    smallest=nums[0]
    for i in range(1, len(nums)):
        if smallest > nums[i]:
            smallest= nums[i]
    print("smallest: " , smallest)

nums= [2,3,1,4,5,2,-1, -5,3,54,-5]
smallest(nums)
