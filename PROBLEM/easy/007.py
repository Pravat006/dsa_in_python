def moveZeros(nums):
    for i in range(len(nums)):
        if nums[i] != 0:
            continue
        elif nums[i] == 0:
            nums.remove(nums[i])
            nums.append(0)
    return nums

nums = [0,1,0,30,0,12]
print(moveZeros(nums))