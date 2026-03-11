'''
47. Remove Specific Character from String
Remove all occurrences of a given character from the input string.

Input:
String: "hello"
Char: 'l'
Output: "heo"
'''
string = "Hello World"
char = "o"

result = string.replace(char, "")
print(result)  
