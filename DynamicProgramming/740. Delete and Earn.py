"""
740. Delete and Earn
Medium

Given an array nums of integers, you can perform operations on the array.

In each operation, you pick any nums[i] and delete it to earn nums[i] points. After, you must delete every element
equal to nums[i] - 1 or nums[i] + 1.

You start with 0 points. Return the maximum number of points you can earn by applying such operations.

Example 1:

Input: nums = [3, 4, 2]
Output: 6
Explanation:
Delete 4 to earn 4 points, consequently 3 is also deleted.
Then, delete 2 to earn 2 points. 6 total points are earned.


Example 2:

Input: nums = [2, 2, 3, 3, 3, 4]
Output: 9
Explanation:
Delete 3 to earn 3 points, deleting both 2's and the 4.
Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
9 total points are earned.


Note:

The length of nums is at most 20000.
Each element nums[i] is an integer in the range [1, 10000].
"""

class Solution:
    def deleteAndEarn(self, nums):
        N = max(nums)
        # 对于数字重复出现的情况，设置一个字典记录删除该数能得多少分
        num_count = [0] * (N+1)
        for num in nums:
            num_count[num] += num

        # dp[i][j] i表示当前的元素 j表示删除该元素1（得分） 或者 被别相邻的元素删除0（不得分）
        dp = [[0 for _ in range(2)] for _ in range(N+1)]

        for i in range(1,N+1):
            # 当前不得分，可能前一个得分，也可能不得分，选最大
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            # 当前得分，前一个必不得分
            dp[i][1] = dp[i-1][0]+num_count[i]

        return max(dp[N][0], dp[N][1])

s = Solution()
print(s.deleteAndEarn([2, 2, 3, 3, 3, 4]))