'''
28. Find Missing Number (1 to N)
Given N and an array of N-1 integers (containing all numbers from 1 to N except one), it finds the missing number using the formula:

Expected Sum = N × (N+1) / 2 — then subtracts the actual array sum to get the missing value.

Example: N=5, array = [1, 2, 4, 5] → Missing = 3
'''


def findMissing(arr):
    last = arr[-1] # last element of current array
    
    tsum= (last*(last+1))//2
    csum=0
    for i in range(len(arr)):
        csum+=arr[i]
    return tsum-csum

print(findMissing([1,3,4,5]))
