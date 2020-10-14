class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums1)):
            if(nums1[i] in nums2 and nums1[i] not in result):
                for j in range(min(nums1.count(nums1[i]), nums2.count(nums1[i]))):
                    result.append(nums1[i])
        return result
