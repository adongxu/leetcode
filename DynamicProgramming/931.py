"""
931. Minimum Falling Path Sum
Medium

Given a square array of integers A, we want the minimum sum of a falling path through A.

A falling path starts at any element in the first row, and chooses one element from each row.  The next row's choice
must be in a column that is different from the previous row's column by at most one.
从上到下 下一层必须与上一层列临近（距离不超过1） 求所有路径里的最小值（这就是三角路径啊）
Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: 12
Explanation:
The possible falling paths are:
[1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
[2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
[3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
The falling path with the smallest sum is [1,4,7], so the answer is 12.

Note:

1 <= A.length == A[0].length <= 100
-100 <= A[i][j] <= 100
"""

class Solution:
    def minFallingPathSum(self, A):
        N = len(A)
        # 状态定义 dp[i][j]:从A[i][j]往下走的最短距离
        # 状态转移方程：
        #           if j == 0:
        #                     dp[i][j] = min(dp[i+1][j+1], dp[i + 1][j]) + A[i][j]
        #                 elif j == N-1:
        #                     dp[i][j] = min(dp[i+1][j-1], dp[i + 1][j]) + A[i][j]
        #                 else:
        #                     dp[i][j] = min(dp[i+1][j-1], dp[i + 1][j],dp[i+1][j+1]) + A[i][j]
        # 基本情况：dp[N-1][j] = A[N-1][j]

        dp = [[0 for _ in range(N)] for _ in range(N)]

        # 基本情况
        for j in range(N):
            dp[N-1][j] = A[N-1][j]

        # 状态转移
        for i in range(N-2,-1,-1):
            for j in range(N):
                if j == 0:
                    dp[i][j] = min(dp[i+1][j+1], dp[i + 1][j]) + A[i][j]
                elif j == N-1:
                    dp[i][j] = min(dp[i+1][j-1], dp[i + 1][j]) + A[i][j]
                else:
                    dp[i][j] = min(dp[i+1][j-1], dp[i + 1][j],dp[i+1][j+1]) + A[i][j]
        # 返回第一行的最小值
        return min(dp[0])

# s = Solution()
# print(s.minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))