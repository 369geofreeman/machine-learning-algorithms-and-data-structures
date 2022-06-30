"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        def ans(ret):
            if len(ret) % 2:
                return ret[len(ret)//2]
            elif len(ret) <= 2:
                return (float(ret[0]) + float(ret[1]))/2
            return (float(ret[(len(ret)-1)//2]) + float(ret[((len(ret)-1)//2)+1]))/2

        if len(nums2) > len(nums1):
            nums1, nums2 = nums2, nums1

        if nums1 == [] and nums2 == []:
            return []
        if nums1 == []:
            return ans(nums2)
        if nums2 == []:
            return ans(nums1)

        if nums1[-1] < nums2[0]:
            ret = nums1 + nums2
            return ans(ret)

        o, t, ret = 0, 0, []

        while o < len(nums1)+1:

            if t >= len(nums2):
                if o < len(nums1):
                    ret.append(nums1[o])
                o += 1
                continue

            elif o >= len(nums1):
                ret.append(nums2[t])
                t += 1
                continue

            elif nums1[o] >= nums2[t]:
                ret.append(nums2[t])
                t += 1

            elif nums1[o] < nums2[t]:
                ret.append(nums1[o])
                o += 1

        # print(ret)
        return ans(ret)
