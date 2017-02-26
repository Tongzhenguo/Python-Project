# coding=utf-8
"""
Given a positive integer num,
write a function which returns True if num is a perfect square else False.
Note: Do not use any built-in library function such as sqrt.
判断一个正数是不是一个完全平方数，比如16=4**2，要求不能使用库函数
Example 1:
Input: 16
Returns: True

Example 2:
Input: 14
Returns: False
"""

"""
Solution1：
1 = 1
4 = 1 + 3
9 = 1 + 3 + 5
16 = 1 + 3 + 5 + 7
25 = 1 + 3 + 5 + 7 + 9
36 = 1 + 3 + 5 + 7 + 9 + 11
....
so 1+3+...+(2n-1) = (2n-1 + 1)n/2 = nn
=>i = [-3 +/- sqrt(9 + 8n)]/4
"""
# class Solution(object):
#     def isPerfectSquare(self, num):
#         i = 1
#         while (num > 0):
#             num -= i
#             i += 2
#         return num == 0
# print Solution().isPerfectSquare(2147483647)

"""
 a more efficient one using binary search whose time complexity is O(log(n)):
"""
# class Solution(object):
#     def isPerfectSquare(self, num):
#         low ,high = 1, num
#         while (low <= high):
#             mid = (low + high) / 2
#             if (mid * mid == num):
#                 return True
#             elif (mid * mid < num):
#                 low = mid + 1
#             else:
#                 high = mid - 1
#         return False

"""
    牛顿迭代法：https://en.wikipedia.org/wiki/Integer_square_root#Using_only_integer_division

"""
class Solution(object):
    def isPerfectSquare(self, num):
        x = num
        while (x * x > num):
            x = (x + num / x) / 2 #牛顿迭代公式
        return x * x == num
# print Solution().isPerfectSquare(1111*1111)