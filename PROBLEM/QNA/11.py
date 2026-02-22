# 11. LCM of Two Numbers

#  lcm = (a*b)/10

def lcm(n1,n2):
    gcd=n1
    a=n2

    while a!=0:
        gcd,a = a, gcd%a
    
    return abs((n1*n2)//gcd)

print(lcm(2,4))
