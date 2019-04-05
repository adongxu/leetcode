"""
932. Beautiful Array
Medium

For some fixed N, an array A is beautiful if it is a permutation of the integers 1, 2, ..., N, such that:

For every i < j, there is no k with i < k < j such that A[k] * 2 = A[i] + A[j].

Given N, return any beautiful array A.  (It is guaranteed that one exists.)

Example 1:

Input: 4
Output: [2,1,4,3]
Example 2:

Input: 5
Output: [3,1,2,5,4]

Note:

1 <= N <= 1000
"""

# 这个问题有一个非常美妙的数学解法。首先我们要证明漂亮数组满足这样几种性质
#
# 减法（减去一个数仍然是漂亮数组）
#
# (A[k]−x)∗2=A[k]∗2−2∗x≠(A[i]−x+A[j]−x) (A[k]-x)*2=A[k]*2 - 2*x \neq(A[i] -x + A[j] - x)(A[k]−x)∗2=A[k]∗2−2∗x
# ̸
# ​
#  =(A[i]−x+A[j]−x)
#
# 乘法（乘上一个数仍然是漂亮数组）
#
# A[k]∗2∗x≠(A[i]+A[j])∗x=A[i]∗x+A[j]∗x A[k]*2*x\neq(A[i]+A[j])*x=A[i]*x+A[j]*xA[k]∗2∗x
# ̸
# ​
#  =(A[i]+A[j])∗x=A[i]∗x+A[j]∗x
#
# 有了上面这两个性质，我们就可以很快解决这个问题了。我们知道一个数组A可以分为奇数部分A1和偶数部分A2。此时我们如果有一个漂亮数组B，
# 我们根据前面的性质知道2*B-1是一个漂亮数组并且是奇数数组，而2*B也是一个漂亮数组并且是偶数数组。那么我们通过2*B+2*B-1必然可以构成
# 任意一个漂亮数组了

class Solution:
    def beautifulArray(self, N):
        ans = [1]
        ans_len = 1
        while ans_len < N:
            ans = [2 * n - 1 for n in ans] + [2 * n for n in ans]
            ans_len *= 2
        return [n for n in ans if n <= N]

