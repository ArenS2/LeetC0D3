class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(len(A)):
            if((A[i] & 1) == 1):
                result.append(A[i])
            else:
                result.insert(0, A[i])
        return result