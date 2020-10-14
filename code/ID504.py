class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        s = ""
        if(str(num)[0] == "-"):
            num *= (-1)
            s += "-"
        while(1):
            s += str(num%7)
            num = num/7
            if(num == 0):
                break
        if(s[0] == "-"):
            return s[0] + s[1:][::-1]
        return s[::-1]