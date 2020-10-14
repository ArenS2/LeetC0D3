def checkword(arr, w, current):
    for i in range(len(w), 0, -1):
        try:
            arr.index(w[:i])
        except:
            return False
    return len(w) > len(current)
    
class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words = sorted(words)
        result = ""
        for i in range(len(words)-1):
            if(words[i] not in words[i+1] or ( len(words[i+1]) - len(words[i]) != 1 )):
                if(checkword(words, words[i], result)):
                    result = words[i]
        if(checkword(words, words[-1], result)):
            result = words[-1]
        return result
    
    