# 5. Reverse a Number

#  124 -> 421

def reverse(n):
    rev= 0
    while n!=0:
        rev= rev*10+ n%10
        n//=10
    return rev

num =2344324832473248932742834792384245
print(reverse(num))