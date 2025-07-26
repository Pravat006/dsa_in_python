# Fibonacci

# Time: (2^n), Space:O(n)
def F(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return F(n-1) + F(n-2)


val= F(30)
print(val)