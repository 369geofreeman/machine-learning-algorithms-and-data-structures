"""
Peak Index in a Mountain Array
Easy

Let's call an array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
Given an integer array arr that is guaranteed to be a mountain, return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

 

Example 1:

Input: arr = [0,1,0]
Output: 1
Example 2:

Input: arr = [0,2,1,0]
Output: 1
Example 3:

Input: arr = [0,10,5,2]
Output: 1
 

Constraints:

3 <= arr.length <= 104
0 <= arr[i] <= 106
arr is guaranteed to be a mountain array.
 

Follow up: Finding the O(n) is straightforward, could you find an O(log(n)) soluti
"""


class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        l = 1
        r = len(arr)-2

        while l <= r:

            m = l + (r - l) // 2

            if arr[m-1] < arr[m] > arr[m+1]:
                return m

            if arr[m-1] < arr[m]:
                l = m + 1
            else:
                r = m - 1
