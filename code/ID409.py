class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        single = []
        for i in range(len(s)):
            if((s[i] not in single) and (s.count(s[i]) > 1)):
                single.append(s[i])
        result = 0
        for i in range(len(single)):
            result += (s.count(single[i])/2)*2
        if(result < len(s)):
            return result + 1
        return result