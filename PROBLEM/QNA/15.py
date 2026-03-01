# 15. Check Anagram

def isAnagram(str1, str2):
    if len(str1) != len(str2):
        return False
    sett= {}
    for char in str1:
        sett[char]= sett.get(char, 0)+1
    for char in str2:
        if char not in sett:
            return False
        sett[char]-=1
    return True

print(isAnagram("abcdw", "abcwd"))