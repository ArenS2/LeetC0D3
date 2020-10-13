def trans(x):
    x = str(x)
    re = 0
    for i in x:
        re += int(i)
    return re
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while(len(str(num)) > 1):
            num = trans(num)
        return num