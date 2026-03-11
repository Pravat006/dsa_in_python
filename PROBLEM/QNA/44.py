'''
44. Count Even and Odd Numbers in Array
Given an array of integers, count how many are even and how many are odd.

Input: 5 → 1 2 3 4 5
Output:
Even: 2
Odd: 3
'''

#NOTE: reminder of even num is 0 and reminder of odd number is 1

arr= [22,3,5,66,7,2,3]
even= 0
for num in arr:
    if num%2==0:
        even+=1

print("Even count: ", even)
print("Odd count: ", len(arr)-even)



