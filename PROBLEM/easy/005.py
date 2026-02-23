# 20. Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


def isValid(strs):
    stack=[]
    strmap = {
        ")": "(",
        "}": "{",
        "]": "["
    }
    #going through each character of the string
    for char in strs:
        #find the char in the strmap values
        if char in strmap.values():
            # print(char)
            stack.append(char)
            # print(stack)

        elif char in strmap.keys():
            print(char)
            print(strmap[char])

            if not stack or strmap[char] != stack.pop():
                return False
        return not stack

str= "}){["
print(isValid(str))