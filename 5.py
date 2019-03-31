"""
5. Longest Palindromic Substring 最长连续回文串
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""
class Solution:
    """
    动态规划
    设字符串为str，长度为n，p[i][j]表示第i到第j个字符间的子序列的个是否是回文串，则：
    状态初始条件：dp[i][i]=True （i=0：n-1） dp[i][i+1]=(dp[i][i] == dp[i][i+1])
    状态转移方程：
    """
    def longestPalindrome(self, s):
        n = len(s)
        # 初始化dp数组
        dp = [[False]*n]*n
        print(dp)

s = Solution()
print(s.longestPalindrome('babad'))

