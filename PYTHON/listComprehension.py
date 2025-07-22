i = [x for x in range(5)] #[0, 1, 2, 3, 4]
j = [x**2 for x in range(5)] #[0, 1, 4, 9, 16]
k = [x for x in range(5) if (x%2)==0 ] #[0, 2, 4]

print(i)
print(j)
print(k)