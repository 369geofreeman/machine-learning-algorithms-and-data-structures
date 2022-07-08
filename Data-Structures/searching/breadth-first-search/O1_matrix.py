"""
01 Matrix
Medium

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
"""

from collections import deque

class Solution:
    def __init__(self):
        self.count = 0
    def updateMatrix(self, A):
        R, C = len(A), len(A[0])
        def neighbors(r, c):
            for cr, cc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                if 0 <= cr < R and 0 <= cc < C:
                    yield cr, cc

        q = deque([((r, c), 0) 
                for r in range(R) 
                for c in range(C) 
                if A[r][c] == 0])
        seen = {x for x,_ in q}
        ans = [[0]*C for _ in A]
        while q:
            (r, c), depth = q.popleft()
            ans[r][c] = depth
            for nei in neighbors(r, c):
                if nei not in seen:
                    seen.add(nei)
                    q.append((nei, depth + 1))

        return ans