# 20: Bubble Sort
'''
Given an array of integers, sort the array in ascending order using the bubble sort algorithm and print the sorted array.

'''

def bubble_sort(arr):
    n = len(arr)
    flag= True

    while flag:
        flag = False
        for i in range(1,n):
            if arr[i-1] > arr[i]:
                flag = True
                arr[i-1], arr[i]= arr[i], arr[i-1]

