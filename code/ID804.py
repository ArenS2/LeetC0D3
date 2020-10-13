import string
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alpha = string.ascii_lowercase
        dcount = 0
        savelist = []
        for i in range(len(words)):
            mstring = ""
            for j in range(len(words[i])):
                position = alpha.find(words[i][j])
                mstring += morse[position]
            if(mstring not in savelist):
                dcount += 1
                savelist.append(mstring)
        return dcount
    