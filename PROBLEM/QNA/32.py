'''
32. Move All Zeros to End
Uses an index pointer to shift all non-zero elements to the front of the array, then fills the remaining positions with zeros. Order of non-zero elements is preserved. Example: [0, 1, 0, 3, 2] → [1, 3, 2, 0, 0]

'''
def moveZeros(arr):
    for i in range(len(arr)):
        if arr[i] == 0:
            zero_value = arr[i]  
            arr.remove(zero_value)
            arr.append(zero_value)
    return arr

arr = [2, 3, 4, 0, 7, 0, 9, 4, 0]
print("before : ", arr)
print("after: ", moveZeros(arr))
