# 6. Check Palindrome Number

def isPalindrome(n):
    original=n
    rev=0
    while n!=0:
        rev= rev*10+ n%10
        n//=10

    if(rev==original):
        return True
    else:
        return False

num=1212
print(isPalindrome(num))