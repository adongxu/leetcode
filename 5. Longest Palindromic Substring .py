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
    状态转移方程：dp[i][j]=dp[i+1][j-1]
    """
    def longestPalindrome(self, s):
        if not s:
            return ""

        n = len(s)
        # 初始化dp数组
        dp = [[False for _ in range(n)] for _ in range(n)]
        # 初始化最大长度和起始索引
        maxlen, start = 1, 0
        # 初始化长度为1的回文串
        for i in range(n):
            dp[i][i] = True
        # 初始化长度为2的回文串
        for i in range(n-1):
            j = i+1
            if s[i] == s[j]:
                dp[i][j] = True
                maxlen = 2
                start = i
        # 长度>=3的回文串
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + (length - 1)
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    start = i
                    maxlen = length
        return s[start:start+maxlen]


