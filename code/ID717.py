class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        while(len(bits) > 1):
            if(bits[0] == 1):
                bits = bits[2:]
            else:
                bits = bits[1:]
        return len(bits) == 1