def shortest(arr, n):
    l =0
    r = 0
    for i in range(len(arr)):
        if(arr[i] == n):
            l = i
            break
    for i in range(len(arr)-1, 0, -1):
        if(arr[i] == n):
            r = i
            break
    return arr[l:r+1] 

def checkdegree(nums):
    temp = []
    for i in range(len(nums)):
        if(nums[i] not in temp):
            temp.append(nums[i])
        
    count_max = 0
    m = []
    for i in range(len(temp)):
        if(nums.count(temp[i]) > count_max ):
            count_max = nums.count(temp[i])
            m.append(temp[i])
    return count_max
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = []
        for i in range(len(nums)):
            if(nums[i] not in temp):
                temp.append(nums[i])
        
        count_max = 0
        m = []
        for i in range(len(temp)):
            if(nums.count(temp[i]) > count_max ):
                count_max = nums.count(temp[i])
                m.append(temp[i])
            if(nums.count(temp[i]) == count_max and temp[i] not in m):
                m.append(temp[i])
        minn = len(nums)
        for i in range(len(m)):
            subarr = shortest(nums, m[i])
            if(len(subarr) < minn and checkdegree(subarr) == count_max ):
                minn = len(subarr)
        return minn