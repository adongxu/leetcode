"""
357. Count Numbers with Unique Digits
Medium

Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10^n.

Example:

Input: 2
Output: 91
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100,
             excluding 11,22,33,44,55,66,77,88,99
"""

class Solution:
    def countNumbersWithUniqueDigits(self, n):
        # 暴力 O(10**n)
        count = 0
        for i in range(10 ** n):
            if len(str(i)) == len(set(str(i))):
                count += 1
        return count

class Solution1:
    def countNumbersWithUniqueDigits(self, n):
        # dp[i]：0-10^i时的数目
        # 状态转移：dp[i]=dp[i-1]+i位数的不重复数目（首位9种情况（去掉0）*次位9种情况（与首位不同但可以取0）
        # *8*7...）
        # 基本情况 dp[1]=10
        if not n:
            return 1
        dp = [0] * (n+1)
        dp[1] = 10
        for i in range(2, n+1):
            val = 9
            for j in range(i-1):
                val *= (9-j)
            dp[i] = dp[i-1]+val
        return dp[-1]

#################画图比较二者的时间复杂度##################################
import time
import matplotlib.pyplot as plt

def cmpTwoFuncs(fn1, fn2):
    fn1_time, fn2_time = [], []
    for n in range(1, 8):
        begin1 = time.time()
        fn1(n)
        end1 = time.time()
        fn1_time.append(end1-begin1)

        begin2 = time.time()
        fn2(n)
        end2 = time.time()
        fn2_time.append(end2 - begin2)

    x = range(1,8)
    plt.plot(x, fn1_time)
    plt.plot(x, fn2_time)
    plt.show()

cmpTwoFuncs(Solution().countNumbersWithUniqueDigits, Solution1().countNumbersWithUniqueDigits)
##############################################################
