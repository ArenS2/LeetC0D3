class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        count = 0
        for i in range(len(ransomNote)):
            if(ransomNote.count(ransomNote[i]) > magazine.count(ransomNote[i])):
                return False
        return True
                