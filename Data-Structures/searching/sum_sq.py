"""
Sum of Square Numbers
Medium

Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

 

Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:

Input: c = 3
Output: false
 

Constraints:

0 <= c <= 231 - 1
"""

from math import sqrt


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """

        if c == 0:
            return True

        l, r = 0, int(sqrt(c))+1

        while l <= r:

            s = (l*l) + (r*r)

            if s == c:
                return True

            if s > c:
                r -= 1
            else:
                l += 1

        return False
