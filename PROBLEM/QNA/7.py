# 7. Armstrong Number

def isAmstrong(num):
    temp=num
    sm=0
    digits=len(str(num))

    while num!=0:
        i= num%10
        sm+= i**digits
        num//=10
    if(temp==sm):
        return True
    else:
        return False
    
num = 1532
print(isAmstrong(num))
