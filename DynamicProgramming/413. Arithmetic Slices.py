"""
413. Arithmetic Slices 等差数列
Medium

A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any
two consecutive elements is the same.

For example, these are arithmetic sequence:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that
0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.


Example:

A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
"""
class Solution:
    def numberOfArithmeticSlices(self, A):
        # 注：这个解法O(n2)在大数时超时了
        # 状态定义:dp[i][j] i->j的序列是否为等差数列
        # 基本情况 j-i<=1 :False
        # 状态转移：dp[i][j] = {if dp[i][j-1]=False:False,if dp[i][j-1]=True and a[j] = a[j-1]+(a[j-1]-a[i])/(j-1-i):True}
        if not A or len(A) <= 2:
            return 0
        N = len(A)
        count = 0
        dp = [[False for _ in range(N)] for _ in range(N)]
        for i in range(N-1,-1,-1):
            for j in range(i,N):
                if j-i<=1:
                    dp[i][j] = False
                elif j-i == 2:
                    if A[j]-A[j-1] == A[j-1]-A[i]:
                        dp[i][j] = True
                        count += 1
                    else:
                        dp[i][j] = False
                else:
                    if dp[i][j-1] and A[j] == A[j-1]+(A[j-1]-A[i])/(j-1-i):
                        dp[i][j] = True
                        count += 1
                    else:
                        dp[i][j] = False
        return count


class Solution1:
    def numberOfArithmeticSlices(self, A):
        # 找规律
        # e.g For [1,2,3] we have [1,2,3]
        # For [1,2,3,4] we have [1,2,3], [1,2,3,4], [2,3,4] ie it adds 2 new sub-arrays ending with 4.
        # For [1,2,3,4,5], we have [1,2,3,4,5], [2,3,4,5], [3,4,5] ie it adds 3 new sub-arrays ending with 5 to whatever we could make with 4 elements ie [1,2,3,4]
        # Likewise for 6 elements, we will have 4 new sub-arrays that'd be added, so on and forth.
        # 3->4 加了一个 4->5加了2个 5->6加了3个
        count = cur = 0
        for i in range(2, len(A)):
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                cur += 1
                count += cur
            else:
                cur = 0
        return count

s= Solution()
print(s.numberOfArithmeticSlices([1, 2, 3, 4,5]))


