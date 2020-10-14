class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        temp = n
        count = 0
        while(1):
            if(temp == 1):
                return True
            result = 0
            for i in str(temp):
                result += pow(int(i), 2)
            temp = result
            count += 1
            if(temp == n or count == 30):
                return False
            