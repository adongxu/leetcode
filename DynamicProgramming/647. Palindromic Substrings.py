"""
647. Palindromic Substrings
Medium

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of
same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Note:

The input string length won't exceed 1000.
"""
class Solution:
    def countSubstrings(self, s):
        # 状态定义：dp[i][j] i->j的字符串是否是回文串
        # 状态转移：dp[i][j]={if i==j:True, if j<i:不管 if i<j:{if s[i] != s[j]:False,否则:
        # if j-i<= 2 or dp[i+1][j-1]=True}}
        N = len(s)
        count = 0
        dp = [[False for _ in range(N)] for _ in range(N)]
        for i in range(N,-1,-1):
            for j in range(i,N):
                if i == j or (s[i] == s[j] and (j-i<=2 or dp[i+1][j-1]==True)):
                    dp[i][j] = True
                    count += 1
        return count