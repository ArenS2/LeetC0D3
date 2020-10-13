class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if(ops == []):
            return m*n
        a1 = []
        a2 = []
        for i in range(len(ops)):
            a1.append(ops[i][0])
            a2.append(ops[i][1])
        return min(a1)*min(a2)