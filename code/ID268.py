class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        for i in range(1, len(nums)):
            if((nums[i] - nums[i-1]) == 2):
                return nums[i]-1
        if(nums[0] == 0):
            return len(nums)
        return 0