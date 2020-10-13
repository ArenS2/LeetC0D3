class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        temp = []
        result = []
        for i in range(len(nums1)):
            if(nums1[i] not in temp):
                temp.append(nums1[i])
                if(nums1[i] in nums2):
                    result.append(nums1[i])
        return result