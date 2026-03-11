'''
39. Power of a Number
Calculate base raised to the power exp using a simple loop (without built-in power functions).

Input: 2 5
Output: 32

'''

base= int(input("Enter the base number: " ))
exp= int(input("Enter the exp number: " ))

res=1
for _ in range(exp):
    res*=base

print(f"power of {base} is {res}")
