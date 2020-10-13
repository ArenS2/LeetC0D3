class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        temp = list(set(nums))
        count = 0
        m = 0
        st = len(nums)/2
        for i in range(len(temp)):
            if(nums.count(temp[i]) > count):
                count = nums.count(temp[i])
                m = temp[i]
        return m