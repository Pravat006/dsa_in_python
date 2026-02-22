# 14. Reverse a String

#  to reverse a string , we can string go through a reverse for loop 
#  join every last char in a reverse varible evry char retrival

def rev_str(text):
    rev=""
    for i in range(len(text)-1, -1, -1):
        rev+=text[i]
    return rev

print(rev_str("hello"))