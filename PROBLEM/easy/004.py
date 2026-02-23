# longest common prefix
def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""
    #taking the first as prefix
    prefix = strs[0]

    #loop through each string in the list except the first one
    for i in range(1,len(strs)):
        current_word = strs[i]

    #while the current word does not start with the prefix
        while not current_word.startswith(prefix):
            #Reduce the prefix by one character from the end
            prefix = prefix[:-1]

            #if the prefix becomes empty then return immediately
            if prefix == "":
                return ""
    #Return the final prefix after checking the all the words
    return prefix


strs = ["flower","flow","floight"]
print(longestCommonPrefix(strs))