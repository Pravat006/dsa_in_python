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


#checking if array has an element - O(n)
if 6 in A:
    print(True)
else:
    print(False)

# STrng
#Append to end of string
s= 'hello'
b= s+' world'
print(b)

#checking if something is in string- O(n)
if 'e' in s:
    print(True)

#Access positions- O(1)
print(s[2])

