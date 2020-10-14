class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = max(nums)
        result = nums.index(max1)
        nums.remove(max1)
        if(len(nums) == 0):
            return 0
        max2 = max(nums)
        if(max1 >= max2*2):
            return result
        return -1