'''
78. Subsets

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n= len(nums)
        res, sol= [], []
        
        def backtrack(i):
            if i==0:
                res.append(sol[:])
                return
            # dont pick nums[i]
            backtrack(i+1)
            # pick nums[i]
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
        backtrack(0)
        
        return res

