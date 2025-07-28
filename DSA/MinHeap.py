# Build min-heap (Heapify)
# Time: O(n), space : O(1)


A= [-4,3,1,0,2,5,10,8,12,9]

import heapq

heapq.heapify(A)

# print(A)

# Heap Push (Insert Element)
#Time: O(log n)

heapq.heappush(A,4)
# print(A)


# Heap pop (Extract min)
# Time: O(log n)

minn= heapq.heappop(A)


# print(minn)

# Heap sort
# Time: O(n log n), Space: O(n)


def heapsort(arr):
    heapq.heapify(arr)
    n= len(arr)
    new_list = [0]*n

    for i in range(n):
        minn = heapq.heappop(arr)
        new_list[i] = minn

    return new_list

res= heapsort([1,8,6,5,7,8,4,15,18,11])
# print(res)

# Heap push pop: Time O(log n)

heapq.heappush(A,100)

# print(A)



# max heap

B= [-4,3,1,0,2,5,10,8,12,9]
n= len(B)

for i in range(n):
    B[i]= -B[i]

heapq.heapify(B)
print(B)





















