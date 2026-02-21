# Two sum

def twoSum(nums,target):
    l=0
    r=len(nums)-1
    while l<r:
        if nums[l]+nums[r]==target:
            return nums[l],nums[r]
        if nums[l]+nums[r]<target:
            l+=1
        elif nums[l]+nums[r]>target:
            r-=1
    return [nums[l],nums[r]]



nums = [2,7,11,15]
target = 11
print(twoSum(nums,target))