class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = min(nums)
        result = 0
        for i in range(len(nums)):
            result = result + nums[i] - m
        return result