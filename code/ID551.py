class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return (s.count("A") < 2) and (len(s) - len(s.replace("LLL", "")) == 0)