'''
50. Two Sum Problem
Given an array and a target, find two numbers that add up to the target. Return their indices (0-based).
If no pair exists, print "No Pair Found".

Input:
Array: 5 → 2 7 11 15
Target: 9
Output: 0 1 (because 2 + 7 = 9)
'''

def find_pair(target, arr):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [arr[left], arr[right]]
        elif current_sum > target:
            right -= 1
        else:
            left += 1
    
    return "No pair found"

target = int(input("Enter target: "))
arr = [2, 3, 4, 5, 9, 12]
result = find_pair(target, arr)
print(result)
