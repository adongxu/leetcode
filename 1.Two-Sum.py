"""
1.Two-Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
class Solution:
    def twoSum(self, nums, target):
        # 哈希法
        dic = {}
        for i,num in enumerate(nums):
            # key-value:当前的数值-(target-num)的索引
            # 如果在就返回
            if num in dic:
                return [dic[num], i]
            # 不在就添加到字典中
            dic[target-num] = i
