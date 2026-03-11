'''
35. Count Number of Digits
Count how many digits are in a given integer by repeatedly dividing it by 10 until it becomes 0, incrementing a counter each time.

Input: 12345
Output: 5

'''

num = int(input("Enter the number: "))

count =0
while num!=0:
    num //=10
    count+=1
print("total digits", count)
