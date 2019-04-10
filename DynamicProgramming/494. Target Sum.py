"""
494. Target Sum
Medium

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -.
For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
"""
import collections
class Solution:
    def findTargetSumWays(self, nums, S):
        # dp {key:value} 和为key的情况出现了value次
        dp = {0: 1}
        for i in nums:
            print('i=',i)
            new = collections.Counter()
            for old in dp:
                # dp[old] 和为old出现的次数
                new[old - i] += dp[old]
                new[old + i] += dp[old]
            dp = new
        return dp[S]

s = Solution()
print(s.findTargetSumWays([1, 1, 1, 1, 1], 3))