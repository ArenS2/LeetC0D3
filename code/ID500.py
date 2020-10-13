from re import sub
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        for i in range(len(words)):
            if( sub("[qwertyuiopQWERTYUIOP]+", "", words[i]) == "" or sub("[asdfghjklASDFGHJKL]+", "", words[i]) == "" or sub("[zxcvbnmZXCVBNM]+", "", words[i]) == ""):
                result.append(words[i])
        return result