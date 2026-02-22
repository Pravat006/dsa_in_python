# 8. Sum of Digits

def sumOfDigits(num):

    sm=0
    while num!=0:
        sm+=num%10
        num//=10
    return sm
n=1226
print(sumOfDigits(n))