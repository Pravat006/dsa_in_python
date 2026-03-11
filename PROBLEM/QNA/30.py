'''
30. Remove All Spaces from String
Reads a string input and removes all space characters using replaceAll(" ", ""), then prints the result. Example: "hello world" → "helloworld"

'''

string= input("Enter the spaced string : ")

res= "".join(char for char in string if char != " ")
print(res)
