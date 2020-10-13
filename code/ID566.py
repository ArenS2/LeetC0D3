class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        newlist = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                newlist.append(nums[i][j])
        
        if(len(newlist) < r*c):
            return nums
        
        result = []
        count = 0
        for i in range(r):
            temp = []
            for _ in range(c):
                temp.append(newlist[count])
                count += 1
            result.append(temp)
        return result