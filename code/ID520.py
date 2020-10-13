import string
from re import sub
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        r = word[1:]
        if(word[0] in string.ascii_lowercase ):
            r = sub("[a-z]+", "", r)
            return len(r) == 0
        else:
            r = sub("[a-z]+", "", r)
            if((len(r) == len(word)-1) or (len(r) == 0)):
                return True
            return False