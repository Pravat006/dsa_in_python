'''
40. Decimal to Binary
Convert a decimal integer to its binary representation by repeatedly taking % 2 and prepending the remainder.

Input: 10
Output: 1010

'''

num= int(input("Enter the number: "))
tmp=num
binary= ""
while num>0:
    binary= str((num%2))+binary
    num//=2
print(f"Binary of {tmp} is {binary}") 
