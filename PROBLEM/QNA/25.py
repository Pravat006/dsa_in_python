#25. Count Frequency of Element inArray

def countFreq(arr,n):
    count=0
    for num in arr:
        if num==n:
            count+=1
    return count
    
nums=[4,2,5,6,22,3,4,8,2,4,5,2,6,2,9,8,2,7,5,4]
print(countFreq(nums, 2))
