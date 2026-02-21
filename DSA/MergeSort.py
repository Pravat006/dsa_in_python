# Merge sort
# Time: O(n log n)
# Space: O(n) - Note: can be Long n, but is harder to write


C= [-3,6,8,-3,-5,8,2,1,6,9,-1]


def merge_sort(arr):
    n= len(arr)

    if  n==1:
        return arr
    middle = len(arr)//2
    left = arr[:middle]
    right= arr[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    l,r= 0,0
    left_len= len(left)
    right_len= len(right)

    sorted_arr= [0]*n
    i= 0
    while l<left_len and r<right_len:
        if left[l]<=right[r]:
            sorted_arr[i]= left[l]
            l +=1
        else:
            sorted_arr[i]= right[r]
            r +=1

        i += 1

    while l< left_len:
        sorted_arr[i]= left[l]
        l +=1
        i += 1
    while r< right_len:
        sorted_arr[i]= right[r]
        r +=1
        i += 1
    return sorted_arr

print(merge_sort(C))
