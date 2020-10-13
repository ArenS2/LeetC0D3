class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        s4m = 0 
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(grid[i][j] == 1):
                    s4m += 4
                if(j < len(grid[i])-1 and grid[i][j] == 1 and grid[i][j+1] == 1):
                    s4m -= 2
        for i in range(len(grid[0])):
            for j in range(len(grid)-1):
                if(grid[j][i] == 1 and grid[j+1][i] == 1):
                    s4m -= 2
        return s4m
        