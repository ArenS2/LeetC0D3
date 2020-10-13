class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = bin(n)[2:]
        for i in range(len(s)-1):
            if(int(s[i])^int(s[i+1]) == 0):
                return False
        return True