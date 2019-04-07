"""
343. Integer Break
Medium

Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of
those integers. Return the maximum product you can get.

给定一个数字 把它分成至少两数的和 求这几个数的乘积的最大值

Example 1:

Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
Note: You may assume that n is not less than 2 and not larger than 58.
"""
class Solution:
    def integerBreak(self, n):
        # dp[i] 整数i的结果
        dp = [1] * n
        for total in range(2, n + 1):
            for i in range(1, total // 2 + 1):
                dp[total - 1] = max(dp[total - 1], max(dp[i - 1], i) * max(dp[total - i - 1], total - i))
        return dp[-1]

s = Solution()
print(s.integerBreak(10))
