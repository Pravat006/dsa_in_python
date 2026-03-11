'''
38. Pattern Printing (Right Triangle)
Print a right-angled triangle pattern of * with n rows, where row i contains i stars.

Input: 4
Output:
*
**
***
****

'''

n= int(input("enter the height : "))

for i in range(1,n+1):
    print("*"*i)



