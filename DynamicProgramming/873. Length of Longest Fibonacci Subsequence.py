"""
873. Length of Longest Fibonacci Subsequence
Medium

A sequence X_1, X_2, ..., X_n is fibonacci-like if:

n >= 3
X_i + X_{i+1} = X_{i+2} for all i + 2 <= n
Given a strictly increasing array A of positive integers forming a sequence, find the length of the longest fibonacci-like subsequence of A.
 If one does not exist, return 0.

(Recall that a subsequence is derived from another sequence A by deleting any number of elements (including none) from A, without changing
the order of the remaining elements.  For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].)

Example 1:

Input: [1,2,3,4,5,6,7,8]
Output: 5
Explanation:
The longest subsequence that is fibonacci-like: [1,2,3,5,8].
Example 2:

Input: [1,3,7,11,12,14,18]
Output: 3
Explanation:
The longest subsequence that is fibonacci-like:
[1,11,12], [3,11,14] or [7,11,18].

Note:

* 3 <= A.length <= 1000
* 21 <= A[0] < A[1] < ... < A[A.length - 1] <= 10^9
* (The time limit has been reduced by 50% for submissions in Java, C, and C++.)
"""
class Solution:
    def lenLongestFibSubseq(self, A):
        dp = {}
        # dp key:fib数列第二和第三个元素 value：数列的长度
        s = set()
        for i in range(len(A)):
            s.add(A[i])
            # A[0],A[1]直接进，A[2]开始执行内循环
            for j in range(1,i):
                # 能否组成A[i]-A[j],A[j],A[i]的形式
                if A[i]-A[j] in s and A[i]-A[j] < A[j]:
                    if (A[i]-A[j], A[j]) in dp:
                        dp[(A[j], A[i])] = dp[(A[i]-A[j], A[j])]+1
                    else:
                        dp[(A[j], A[i])] = 3
        return max(dp.values()) if dp else 0

S = Solution()
print(S.lenLongestFibSubseq([1,3,7,11,12,14,18]))
