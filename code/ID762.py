def check(n):
    s = bin(n)[2:]
    x = 0
    for i in range(len(s)):
        x += int(s[i])
    if(x < 2):
        return False
    if(x == 2 or x == 3):
        return True
    for i in range(2, x):
        if(x%i == 0):
            return False
    return True

class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        count = 0
        for i in range(L, R+1):
            if(check(i)):
                count += 1
        return count