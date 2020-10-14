class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if(len(nums)>1):
            result = 0
            temp = 1
            for i in range(len(nums)-1):
                if(nums[i] < nums[i+1]):
                    temp += 1
                else:
                    result = max(result, temp)
                    temp = 1
            return max(result,temp)
        elif(len(nums) == 0):
            return 0
        return 1
        