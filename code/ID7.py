class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if(x == 0):
            return x
        if(x>0):
            sign = ""
        else:
            sign= "-"
            x = abs(x)
        x = int(str(x)[::-1])
        if( (x> (pow(2,31)-1))  or (x < -2**31) ):
            return 0
        return sign + str(x)