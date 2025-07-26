# Condition based binary search

B= [False,False,False,False,False,True,True,True]

def binary_search_condition(arr):
    N= len(arr)
    L= 0
    R= N-1
    while L<R:
        M= (L+R)//2

        if B[M]:
            R=M
        else:
            L= M+1
    return L

res=binary_search_condition(B)
print(res)
