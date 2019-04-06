"""
53. Maximum Subarray
Easy

Given an integer array nums, find the contiguous subarray (containing at least one number) which has 
the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, 
which is more subtle.
"""
class Solution:
    def maxSubArray(self, nums):
        # 如果前一个加起来比本身的值大，就合在一起，否则保持不变
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i]+nums[i-1])
        return max(nums)

s= Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))