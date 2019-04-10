"""
96. Unique Binary Search Trees
Medium

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

class Solution:
    def numTrees(self, n):
        # dp[i] 1->i时的二叉树的数量
        dp = [0 for _ in range(n+1)]
        # 初始化
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            # j就是1->i这几个数中哪个数作为树根
            for j in range(1,i+1):
                # 左子树的根 j-1 右子树的根i-j
                dp[i] += dp[j-1]*dp[i-j]
        return dp[n]

s= Solution()
print(s.numTrees(3))


