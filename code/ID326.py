from math import log

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n == 1):
            return True
        try:
            temp = round(log(n, 3))
        except:
            return False
        return pow(3, temp) == n