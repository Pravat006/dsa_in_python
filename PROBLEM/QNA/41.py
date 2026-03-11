'''
41. Binary to Decimal
Convert a binary string (e.g., "1010") to its decimal equivalent by processing each digit from right to left, multiplying by powers of 2.

Input: 1010
Output: 10
'''

binary= input("Enter the binary in 0's and 1's : ")

dec=0

for i in range(len(binary)-1, -1, -1):
    if binary[i]=="1":
        dec+= 2**(len(binary)-1-i)

print(f"binary of {binary} is {dec}")

