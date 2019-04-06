"""
4. Median of Two Sorted Arrays
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        def findMedian(nums):
            # 偶数
            if len(nums)%2 == 0:
                return (nums[len(nums)//2]+nums[(len(nums)//2)-1])/2
            else:
                return nums[len(nums) // 2]

        if not nums1:
            return findMedian(nums2)
        elif not nums2:
            return findMedian(nums1)
        else:
            sum_ls = []
            i = j = 0
            while i<len(nums1) and j<len(nums2):
                if nums1[i]<nums2[j]:
                    sum_ls.append(nums1[i])
                    i += 1
                else:
                    sum_ls.append(nums2[j])
                    j += 1
            sum_ls.extend(nums1[i:])
            sum_ls.extend(nums2[j:])
            print(sum_ls)
            return findMedian(sum_ls)