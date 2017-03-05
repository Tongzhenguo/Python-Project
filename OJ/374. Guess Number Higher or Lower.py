# coding=utf-8
"""
We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I'll tell you whether the number is higher or lower.
You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):
-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example:
n = 10, I pick 6.
Return 6.
设计一个猜数游戏算法，从1到n中选出一个数，每次猜错提示高了（1）还是低了（-1），直到猜中返回正确的数字
其中预定义一个函数guess(int num)：
 如果正确的数字比num小，返回-1；比num大，返回1，相等返回0
"""


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num):
    if num == 6: return 0
    elif num > 6:return 1
    else :return -1
class Solution(object):
    def guessNumber(self, n):
        """
        折半查找
        """
        low = 1
        high = n
        while( low <= high ):
            mid = ( low + high ) / 2
            if guess(mid) == 0:
                return mid
            elif guess( mid ) == -1:
                high = mid-1
            else:
                low = mid+1
print Solution().guessNumber(10)
