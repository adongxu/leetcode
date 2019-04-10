"""
718. Maximum Length of Repeated Subarray 最长公共子序列
Medium

Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:

Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation:
The repeated subarray with maximum length is [3, 2, 1].

Note:

1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100
"""


class Solution:
    def findLength(self, A, B):
        dp = [0] * (len(B)+1)
        res = 0
        for i in range(len(A)):
            for j in range(len(B)-1,-1,-1):
                dp[j+1] = dp[j]+1 if A[i] == B[j] else 0
            print(dp)
            res = max(res, max(dp))
        return res

s= Solution()
print(s.findLength([1,2,3,2,1], [3,2,1,4,7]))


