"""
Count Negative Numbers in a Sorted Matrix
Easy

2382

78

Add to List

Share
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

 

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100
 

Follow up: Could you find an O(n + m) solution?
"""


class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        c = 0

        for row in grid:
            if row[0] < 0:
                c += len(row)

            elif row[-1] < 0:
                for x in range(len(row)):
                    if row[x] < 0:
                        c += len(row) - x
                        break

        return c
