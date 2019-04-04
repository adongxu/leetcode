"""
303. Range Sum Query - Immutable
Easy

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.

 # Your NumArray object will be instantiated and called as such:
    # obj = NumArray(nums)
    # param_1 = obj.sumRange(i,j)
"""
# 关键是多次调用函数 所以要用动态规划 上来就保存结果
class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """

        # Initiate variables
        total = 0
        self.nums = nums
        self.cache = []

        # Cache will contain the sum up to the index position
        # i.e. cache[i] = nums[0] + nums[1] + ... + nums[i]
        for i in nums:
            total += i
            self.cache.append(total)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """

        # Mathematical formula:
        # Play around with x1 + x2 + ... + xj - x1 +...+ xi
        # You'll need the extra "xi" since it's inclusive
        return self.cache[j] - self.cache[i] + self.nums[i]

obj = NumArray([-2, 0, 3, -5, 2, -1])
param_1 = obj.sumRange(2,5)
print(param_1)