from copy import deepcopy

class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
        minn = min(nums)
        for i in range(len(nums)):
            nums[i] = nums[i] - minn
        
        reward = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        for i in range(4, len(nums)+1):
            reward.append(str(i))
            
        temp = deepcopy(nums)
        
        for i in range(len(nums)):
            ind = nums.index(max(temp))
            temp.remove(max(temp))
            nums[ind] = reward[i]
        return nums