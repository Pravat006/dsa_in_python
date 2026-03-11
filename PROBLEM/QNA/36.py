'''
36. Sum of Elements in Array
Read an array of n integers and return the total sum of all elements.

Input: 5 → 1 2 3 4 5
Output: 15
'''

def stotal(arr):
    if len(arr)==0:
        return 0
    total=0
    for num in arr:
        total+=num
    return total
nums=[1,41,1,1,2,2,1,1]

print("Total :", stotal(nums))


