# 9. Palindrome Number


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 10:
            return False

        reversedNum = 0
        temp = x

        while temp:
            reminder = temp % 10
            reversedNum = reversedNum * 10 + reminder
            temp = temp // 10
        return reversedNum == x

