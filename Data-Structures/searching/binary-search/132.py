"""
132 Pattern
Medium

Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

 

Example 1:

Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.
Example 2:

Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:

Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
 

Constraints:

n == nums.length
1 <= n <= 2 * 105
-109 <= nums[i] <= 109
"""


class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        prev = [[nums[0], nums[0]]]
        for n in nums:
            for low, high in prev:
                if low < n < high:
                    return True
            if n < prev[-1][0]:
                prev.append([n, n])
            elif n > prev[-1][1]:
                if len(prev) > 1 and n > prev[-2][0]:
                    prev[-1][0] = prev.pop()[0]
                    prev[-1][1] = n
                else:
                    prev[-1][1] = n
        return False
