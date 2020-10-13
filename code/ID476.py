class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        mask = int("0b" + "1"*len(bin(num)[2:]), 2)
        return mask^num