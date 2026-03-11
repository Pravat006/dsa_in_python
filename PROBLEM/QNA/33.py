'''
33. Rotate Array Right by 1 Position

Saves the last element, shifts all elements one position to the right, then places the saved element at index 0. Example: [1, 2, 3, 4] → [4, 1, 2, 3]
'''


def rotateRight(arr):
    if len(arr)<= 1:
        return arr
    last = arr.pop()
    arr.insert(0, last)
    return arr
arr=[1,3,4,5]
print(rotateRight(arr))
