# 9. Largest of Three Numbers

def largest(a,b,c):
    if (a> b and b>c):
        return a
    elif(b>c):
        return b
    else:
        return c

print(largest(8,46,3))