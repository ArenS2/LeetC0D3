class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums1)):
            check = 0
            for j in range(nums2.index(nums1[i]), len(nums2)):
                if(nums2[j] > nums1[i]):
                    result.append(nums2[j])
                    check += 1
                    break
            if(check == 0):
                result.append(-1)
        return result