A= [1,2,3]
print(A)
#Append -Insert element at end of array- On average: O(1)
A.append(4)
print(A)
#pop -Deleting element at end of array- On average: O(1)
A.pop(3)
print(A)
#Insert (not at end of array)- o(n)
A.insert(2,5)
print(A)
#Modify an element- O(1)
A[0]= 7
print(A)
#Accessing element given index i - o(1)
print(A[2])

