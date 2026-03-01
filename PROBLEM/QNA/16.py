# 16. Remove Duplicates fromString

def removeDuplicate(strg):
    result=""
    sett={}

    for char in strg:
        #  if any dulpicate string frequency found , do not append to result
        if sett.get(char,0)>0:
            continue
        sett[char]= sett.get(char,0)+1
        result+=char
    return result


print(removeDuplicate("abbfffcde"))