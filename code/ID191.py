class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n >= 0):
            return bin(n).count("1")
        else:
            n = abs(n)
            n = bin(n)[2:] + "1"(32 - len(bin(n)[2:]))
            return n.count("1")