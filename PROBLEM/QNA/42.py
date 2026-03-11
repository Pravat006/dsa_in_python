'''
42. Check Perfect Number
A number is perfect if the sum of its proper divisors (excluding itself) equals the number.
Check if the given number is perfect.

Input: 6 → divisors: 1, 2, 3 → sum = 6 → ✅ Perfect
Output: Perfect
'''

num = int(input("Enter the number: "))

total= 0
for i in range(1,num//2+1):
    if num%i==0:
        total+=i
print("Perfect" if num==total else "Not perfect ")

