from math import log

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n == 1):
            return True
        try:
            temp = int(log(n, 2))
        except:
            return False
        return pow(2, temp) == n