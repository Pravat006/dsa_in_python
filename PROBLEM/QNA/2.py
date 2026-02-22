# 2. Check Prime Number


def isPrime(num):
    if num<=1:
        return True
    i=2
    while i*i<=num:
        if num%i==0:
            return False
        i+=1
    return True

num=4
print(isPrime(num))