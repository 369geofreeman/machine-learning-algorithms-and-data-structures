"""
Search Insert Position
Easy

8412

429

Add to List

Share
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)

        l, r = 0, len(nums)-1

        while l <= r:

            mid = l+(r-l)//2

            if nums[mid] == target:
                return mid
            if nums[mid-1] < target and nums[mid] > target:
                return mid

            if nums[mid] > target:
                r = mid
            else:
                l = mid + 1
