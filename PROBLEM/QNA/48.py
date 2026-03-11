'''
48. Sum of Prime Numbers up to N
Calculate the sum of all prime numbers from 2 to N (inclusive).

Input: 10 → primes: 2, 3, 5, 7 → sum = 17
Output: 17
'''

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter the number : "))
total=0
for i in range(num):
    if is_prime(i):
        total+=i
print("SUM: " , total)
