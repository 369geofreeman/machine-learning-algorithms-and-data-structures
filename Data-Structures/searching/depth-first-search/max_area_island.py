"""
Max Area of Island
Medium

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 
Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
"""

from typing import List


class Solution:

    def __init__(self):
        self.l_count = 0
        self.g_count = 0

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        r, c = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= r or j < 0 or j >= c:
                return

            if grid[i][j] == '#' or grid[i][j] == 0:
                return

            if grid[i][j] == 1:
                self.l_count += 1
                grid[i][j] = "#"

            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    dfs(i, j)
                    self.g_count = self.l_count if self.l_count > self.g_count else self.g_count
                    self.l_count = 0

        return self.g_count
