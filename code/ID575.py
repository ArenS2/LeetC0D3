class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        temp = []
        l = len(candies)
        for i in range(l):
            if(candies[i] not in temp):
                temp.append(candies[i])
            if(len(temp) == l/2):
                return l/2
        return len(temp)