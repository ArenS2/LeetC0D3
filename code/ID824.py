def GoatLatin(s):
    vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    if(s[0] in vowel):
        return s + "ma"
    else:
        return s[1:] + s[0] + "ma"
    
class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        result = []
        l = S.split(" ")
        for i in range(len(l)):
            result.append(GoatLatin(l[i]) + "a"*(i+1))
        return " ".join(result)
        