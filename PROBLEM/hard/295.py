'''
295. Find Median from Data Stream

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 
 '''
import heapq
class MedianFinder(object):

    def __init__(self):
        # max heap
        self.left-[]
        #min heap
        self.right=[]
        
    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # construct the left heap as a max heap
        heapq.heappush(self.left, -num)
        
        left_max= -heapq.heappop(self.left)
        
        # construct the right side heap a min heap 
        heapq.heappush(self.right, left_max)
        
        if len(self.right)> len(self.left) :
            # pop the minimum of right half haep and push to left heap
            right_min= heapq.heappop(self.right)
            heapq.heappush(self.left, -right_min)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.left) > len(self.right):
            # max of the max heap
            return -self.left[0]
        return (-self.left[0] + self.right[0])/2.0
            


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
