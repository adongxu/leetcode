"""
Given two strings s1, s2, find the lowest ASCII sum of deleted characters to make two strings equal.
Medium

Example 1:
Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.

Example 2:
Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
Note:

0 < s1.length, s2.length <= 1000.
All elements of each string will have an ASCII value in [97, 122].
"""

class Solution:
    def minimumDeleteSum(self, s1, s2):
        # 状态定义：dp[i][j] s1:0->i s2:0->j时，的最小ascii值
        # 基本情况：dp[0][0]=0
        # 状态转移：每次去除i-1或j-1
        m,n = len(s1), len(s2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if i + j == 0:
                    continue
                if i == 0 and j >0:
                    dp[i][j] = dp[i][j-1]+ord(s2[j-1])
                elif i > 0 and j==0:
                    dp[i][j] = dp[i-1][j]+ord(s1[i-1])
                # 匹配，无需删除
                elif s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                # 删除s2[j-1]和s1[j-1]较小者
                else:
                    dp[i][j] = min(dp[i][j-1]+ord(s2[j-1]),dp[i-1][j]+ord(s1[i-1]))

        return dp[m][n]

s= Solution()
print(s.minimumDeleteSum( s1="delete", s2 = "leet"))