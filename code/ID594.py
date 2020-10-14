class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        single = []
        for i in range(len(nums)):
            if(nums[i] not in single):
                single.append(nums[i])
        single.sort()
        result = []
        for i in range(len(single) -1):
            if(single[i+1] - single[i] == 1):
                leng = nums.count(single[i]) + nums.count(single[i+1])
                result.append(leng)
        if(len(result) == 0):
            return 0
        return max(result)