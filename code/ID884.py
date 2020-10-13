from copy import deepcopy
def returnW(l):
    result = []
    for i in range(len(l)):
        temp = deepcopy(l)
        check = 0
        bk = temp.pop(i)
        for j in range(len(temp)):
            if(bk == temp[j]):
                check = 1
                break
        if(check != 1):
            result.append(bk)
    return result
        
class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        a = A.split(" ")
        b = B.split(" ")
        return returnW(a + b)