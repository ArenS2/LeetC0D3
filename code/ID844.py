from re import sub
def bspace(s):
    while("#" in s):
        if(s[0] == "#"):
            s = s[1:]
        s = sub("[a-z]#", "", s)
    return s

class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        return bspace(S) == bspace(T)
         