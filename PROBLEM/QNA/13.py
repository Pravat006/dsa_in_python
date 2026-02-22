# 13. Count Vowels and Consonants


def count_vc(text):
    volwel=0
    consonant=0

    for ch in text.lower():
        if ch.isalpha():
            if ch in 'aeiou':
                volwel+=1
            else:
                consonant+=1
    return volwel , consonant

v,c= count_vc("aewi22ou")

print("vowel: ", v)
print("consonant: ", c)