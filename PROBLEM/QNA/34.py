'''
34. Check Palindrome String
Builds a reversed version of the input string character by character, then compares it to the original using .equals(). Prints "Palindrome" or "Not Palindrome".


'''

s = input().strip()
rev = ""
for i in range(len(s) - 1, -1, -1):
    rev += s[i]
print("Palindrome" if s == rev else "Not Palindrome")
