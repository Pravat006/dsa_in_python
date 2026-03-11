'''
23: Matrix Addition Given two matrices of size R×C, write a program to compute their element-wise sum and print the resulting matrix.

Input: Number of rows r and columns c, followed by elements of matrix A, then matrix B.
Output: The resulting matrix after addition, printed row by row.
'''

row= int(input("Enter number of rows: "))
col= int(input("Enter number of cols: "))

A=[[0 for _ in range(col)] for _ in range(row)]
B=[[0 for _ in range(col)] for _ in range(row)]
res=[[0 for _ in range(col)] for _ in range(row)]

for i in range(row):
    for j in range(col):
        A[i][j]= int(input(f"enter value for position   {[i]} {[j]} : "))

for i in range(row):
    for j in range(col):
        B[i][j]= int(input(f"enter value for position   {[i]} {[j]} : "))


for i in range(row):
    for j in range(col):
        res[i][j]= A[i][j] + B[i][j]
        
print(res)
