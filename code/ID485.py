class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(0)
        maxx = 0
        while(True):
            index = nums.index(0)
            if(maxx <= index):
                maxx = index
            if(index == len(nums)-1):
                break
            nums = nums[(index+1):]
                
        return maxx
            