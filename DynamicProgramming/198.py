"""
198. House Robber
Easy
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected 
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount 
of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
"""
class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        dp = [[0 for _ in range(2)] for i in range(len(nums))]
        # dp[i][j] j=1,偷第i个屋子;j=0,不偷第i个屋子
        dp[0][0], dp[0][1] = 0, nums[0]
        res = max(dp[0][0], dp[0][1])
        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            dp[i][1] = dp[i-1][0]+nums[i]
            res = max(res, dp[i][0], dp[i][1])
        return res

s =Solution()
print(s.rob([2,7,9,3,1]))