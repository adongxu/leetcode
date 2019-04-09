"""
516. Longest Palindromic Subsequence
Medium

Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of
 s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".
"""
# __B B B A B
# B 1 2 3 3 4
# B 0 1 2 2 3
# B 0 0 1 1 3
# A 0 0 0 1 1
# B 0 0 0 0 1

class Solution:
    def longestPalindromeSubseq(self, s):
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)-1,-1,-1):
            for j in range(i,len(s)):
                if i == j:
                    dp[i][j] =1
                elif s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]+2
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        return dp[0][len(s)-1]
s=Solution()
print(s.longestPalindromeSubseq("bbbab"))
