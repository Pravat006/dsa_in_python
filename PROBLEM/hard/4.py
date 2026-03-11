'''
4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

'''

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):

        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n1, n2 = len(nums1), len(nums2)

        low = 0
        high = n1

        while low <= high:

            partN1 = (low + high) // 2
            partN2 = (n1 + n2 + 1) // 2 - partN1

            maxLN1 = float("-inf") if partN1 == 0 else nums1[partN1 - 1]
            minRN1 = float("inf") if partN1 == n1 else nums1[partN1]

            maxLN2 = float("-inf") if partN2 == 0 else nums2[partN2 - 1]
            minRN2 = float("inf") if partN2 == n2 else nums2[partN2]

            if maxLN1 <= minRN2 and maxLN2 <= minRN1:

                if (n1 + n2) % 2 == 0:
                    return (max(maxLN1, maxLN2) + min(minRN1, minRN2)) / 2.0
                else:
                    return max(maxLN1, maxLN2)

            elif maxLN1 > minRN2:
                high = partN1 - 1
            else:
                low = partN1 + 1
            
            
