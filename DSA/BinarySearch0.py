A= [-3,-1,0,1,4,7]

#Naive O(n) searching
# if 7 in A:
#     print("Yes")

#Traditional Binary Search - Looking up if number is in array
# Time: O(log n)
#Space: O(1)


def binary_search(arr,target):
    N= len(A)
    L= 0
    R= N-1
    while L<=R:
        M= L+((R-L)//2)
        if arr[M]== target:
            return True
        elif target < arr[M]:
            R= M-1
        else:
            L= M+1


    return "Target not found"

res=binary_search(A,5)
print(res)