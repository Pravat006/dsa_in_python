'''
29. Count Words in a String
Reads a line of text, trims leading/trailing spaces, and counts the number of words by splitting on one or more whitespace characters (\\s+). Returns 0 for an empty string.

Example: "Hello World Java" → 3
'''

def cw(str):
    count =0
    inWord=False
    
    for char in str:
        if char!=' ' and not inWord:
            count+=1
            inWord= True
        elif char==' ':
            inWord= False
    return count

print(cw("hw ll oew"))
