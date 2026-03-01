# 17. Find Second Largest inArray

def find(arr):

    first= 0
    sec=0

    for num in arr:
        if num > first:
            sec= first
            first = num
        elif( num>sec and num!=first):
            sec=num
    
    return sec

print(find([2,5,25,40,44,26,38,42]))


