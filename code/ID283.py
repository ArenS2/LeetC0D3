from copy import deepcopy
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        c = deepcopy(nums)
        l = len(nums)
        for i in c:
            if(i == 0):
                nums.remove(i)
        for i in range(l-len(nums)):
            nums.append(0)
        return nums