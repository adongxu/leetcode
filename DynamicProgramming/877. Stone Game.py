"""
877. Stone Game
Medium

Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row,
and each pile has a positive integer number of stones piles[i].
The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.

Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either
the beginning or the end of the row.  This continues until there are no more piles left, at which point the person
with the most stones wins.

Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.

Example 1:

Input: [5,3,4,5]
Output: true
Explanation:
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.


Note:

2 <= piles.length <= 500
piles.length is even.
1 <= piles[i] <= 500
sum(piles) is odd.
"""

# DP思路：
# 状态定义：dp[i][j]为piles[i,j]的情况进行游戏，Alex能获得的最大石头数
# 状态转移方程：dp[i][j] = max(dp[i+1][j]+piles[i], dp[i][j-1]+piles[j])
# 基本情况：dp[i][i] = piles[i], dp[i][i+1] = max(piles[i],piles[i+1])
# 0 1 2 3 4 5       j:0->n 从左至右
# 1 1 2 3 4 5       i:j->0 从下到上
# 2 1 2 3 4 5       其实就是填充上三角矩阵
# 3 1 2 3 4 5
# 4 1 2 3 4 5
# 5 1 2 3 4 5

class Solution:
    def stoneGame(self, piles):
        # 石头的总数
        totalStones = sum(piles)
        # 定义dp
        dp = [[0 for _ in range(len(piles))] for _ in range(len(piles))]

        # 状态转移
        for j in range(len(piles)):
            for i in range(j, -1, -1):
                if i == j:
                    dp[i][j] = piles[i]
                elif i == j -1:
                    dp[i][j] = max(piles[i], piles[j])
                else:
                    dp[i][j] = max(dp[i+1][j]+piles[i], dp[i][j-1]+piles[j])

        return True if dp[0][len(piles)-1] > totalStones / 2 else False
#
# s = Solution()
# print(s.stoneGame([5,3,4,5]))