class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xors = x^y
        count = 0
        for i in range(len(bin(xors)[2:])):
            if(bin(xors)[2:][i] == "1"):
                count += 1
        return count
    