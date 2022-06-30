"""
Valid Perfect Square
Easy

2487

241

Add to List

Share
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

 

Example 1:

Input: num = 16
Output: true
Example 2:

Input: num = 14
Output: false
 

Constraints:

1 <= num <= 2^31 - 1
"""


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        return num**0.5==int(num**0.5)
        
#         low = 1
#         high = num
        
#         while low <= high:
            
#             mid = low+(high-low)//2
            
#             if mid*mid == num:
#                 return True
            
#             elif mid*mid > num:
#                 high = mid - 1
#             else:
#                 low = mid + 1
        
#         return False