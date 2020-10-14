class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n == 2 or n == 1):
            return n
        first = 1
        second = 2
        result = 0
        for i in range(3, n+1):
            result = first + second
            first = second
            second = result
        return result
        