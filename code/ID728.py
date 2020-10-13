def isDivisible(x):
    for i in range(len(str(x))):
        if(str(x)[i] == "0" or x%int(str(x)[i]) != 0):
            return "no"
    return "yes"


class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for i in range(left, right+1):
            if(isDivisible(i) == "yes"):
                result.append(i)
        return result
