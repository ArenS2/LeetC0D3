def FI(l):
    tmp = []
    for i in range(len(l)):
        tmp.append(l[len(l)-1-i] ^ 1)
    return tmp
    
class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(A)):
            A[i] = FI(A[i])
        return A