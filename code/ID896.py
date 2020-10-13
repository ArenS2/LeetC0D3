class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        return (sorted(A) == A) or (sorted(A, reverse=True) == A)