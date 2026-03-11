'''
31. Find Duplicate Elements in Array

Uses a nested loop to compare each element with every subsequent element. If a match is found, it prints that element once (using break to avoid reprinting).

'''

def fndDuplicate(arr):
    for i in range(len(arr)):
        for  j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                print("found duplicate: ", arr[i])
                break
                
                
arr=[1,2,3,2,3,2,5,67,8,8,9]
fndDuplicate(arr)
