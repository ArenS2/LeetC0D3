class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp = set(range(1, len(nums)+1))
        return temp - set(nums)