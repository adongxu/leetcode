"""
62. Unique Paths
Medium

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner
of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
"""
class Solution:
    def uniquePaths(self, m, n):
        # bottom-top dp solution
        # dp[i][j] indicates the total paths at position i,j
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(n-1,-1,-1):
                if i == m-1 or j == n-1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i+1][j]+dp[i][j+1]
        return dp[0][0]

s= Solution()
print(s.uniquePaths(7,3))