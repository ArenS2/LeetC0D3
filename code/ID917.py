import string
class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        d = string.ascii_lowercase + string.ascii_uppercase
        newstr = ""
        for i in S:
            if(i in d):
                newstr += i
        newstr = newstr[::-1]
        result = ""
        j = 0
        for i in S:
            if(i in d):
                result += newstr[j]
                j += 1
            else:
                result += i
        return result