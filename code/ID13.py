class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        result = 0
        for i in range(len(s)-1):
            if(l[s[i]] >= l[s[i+1]]):
                result += l[s[i]]
            else:
                result -= l[s[i]]
        return result + l[s[-1]]