'''
24: Transpose of a Matrix Given a matrix of size R×C, write a program to compute and print its transpose (i.e., convert rows into columns).

Input: Number of rows r and columns c, followed by the matrix elements.
Output: The transposed matrix printed row by row.
'''


row= int(input("Enter number of rows: "))
col= int(input("Enter number of cols: "))

A=[[0 for _ in range(col)] for _ in range(row)]

for i in range(row):
    for j in range(col):
        A[i][j]= int(input(f"enter value for position   {[i]} {[j]} : "))
for j in range(col):
    for i in range(row):
        print(A[i][j], end=" ")
    print()
