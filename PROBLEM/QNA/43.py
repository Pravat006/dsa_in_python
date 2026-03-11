'''
43. Strong Number
A number is strong if the sum of the factorials of its digits equals the number itself.
Example: 145 → 1! + 4! + 5! = 1 + 24 + 120 = 145 → Strong.

Input: 145
Output: Strong

'''
import math

num = int(input("Enter the number "))
tmp, total= num , 0

while num >0:
    digit = num%10
    total+= math.factorial(digit)
    num//=10

print("Strong" if tmp==total else "Not strong")
