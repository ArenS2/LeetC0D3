class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if(len(s) != len(t)):
            return False
        for i in range(len(t)):
            if(t[i] not in s or t.count(t[i]) != s.count(t[i])):
                return False
        return True