"""
338. Counting Bits
Medium

Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's
in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in
linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
"""
class Solution:
    def countBits(self, num):
        # 1.普通方法：位运算，每个数进行一次 大量重复计算
        res = []
        for n in range(num+1):
            count = 0
            while n:
                count += 1
                n = n & (n-1)
            res.append(count)
        return res

class Solution2:
    def countBits(self, num):
        # 2.动态规划 基于奇数索引和偶数索引
        dp = [0] * (num+1)
        dp[0] = 0
        for i in range(1, num+1):
            if i % 2 == 0:
                dp[i] = dp[i // 2]
            else:
                dp[i] = 1 + dp[i//2]
        return dp

class Solution3:
    def countBits(self, num):
        count = [0]*(num+1)
        for i in range(1, num+1):
            # 3.去除最末尾一个1后那个数的1的个数再加1
            count[i] = count[i&(i-1)]+1
        return count