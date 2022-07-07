"""
Find First and Last Position of Element in Sorted Array
Medium

11373

306

Add to List

Share
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        import array

        l, r = -1, -1
        p1, p2 = 0, len(nums)-1
        p1true, p2true = True, True

        for _ in range(len(nums)):
            if p1true and nums[p1] == target:
                l = p1
                p1true = False
            else:
                p1 += 1

            if p2true and nums[p2] == target:
                r = p2
                p2true = False
            else:
                p2 -= 1

        return [l, r]
