from copy import deepcopy
def calc(arr, x, y):
    average = 0
    around = [-1, 0, 1]
    count = 0
    for i in around:
        for j in around:
            if( (x+i >= 0 and x+i < len(arr)) and (y+j >= 0 and y+j < len(arr[0])) ):
                average += arr[x+i][y+j]
                count += 1
    return average/count    
    
class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        N = deepcopy(M)
        for i in range(len(M)):
            for j in range(len(M[i])):
                M[i][j] = calc(N, i, j)
        return M
    