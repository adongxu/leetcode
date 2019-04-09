"""
64. Minimum Path Sum
Medium

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes
the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

class Solution:
    def minPathSum(self, grid):
        # 自底向上求和
        if not grid:
            return 0
        m,n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        # 右下角为本身
        dp[m-1][n-1] = grid[m-1][n-1]
        # 最下
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i == m-1 and j == n-1:
                    continue
                if i == m-1:
                    dp[i][j] = dp[i][j+1]+grid[i][j]
                elif j == n-1:
                    dp[i][j] = dp[i+1][j]+grid[i][j]
                else:
                    dp[i][j] = min(dp[i+1][j], dp[i][j+1])+grid[i][j]

        return dp[0][0]

s = Solution()
print(s.minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))
