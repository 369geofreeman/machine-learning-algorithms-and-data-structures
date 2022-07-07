"""
Minimum Operations to Reduce X to Zero
Medium

You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

 

Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
Example 2:

Input: nums = [5,6,7,8,9], x = 4
Output: -1
Example 3:

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 104
1 <= x <= 109
Accepted
97,668

"""


class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """

        arr_sum = sum(nums)
        if arr_sum < x:
            return -1
        if arr_sum == x:
            return len(nums)

        required_subarray_sum = arr_sum - x
        left = curr_sum = max_subarray_size = 0
        for right, num in enumerate(nums):
            curr_sum += num
            while curr_sum > required_subarray_sum:
                curr_sum -= nums[left]
                left += 1
            if curr_sum == required_subarray_sum:
                max_subarray_size = max(max_subarray_size, right - left + 1)

        return len(nums) - max_subarray_size if max_subarray_size > 0 else -1
