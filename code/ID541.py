class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        new = ""
        while(1):
            if(len(s) == 0):
                return new
            temp = s[0:2*k]
            new += temp[0:k][::-1] + temp[k:]
            s = s[2*k:]