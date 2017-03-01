# coding=utf-8
__author__ = 'arachis'
"""
Implement int sqrt(int x).
自己实现int sqrt(int x)
"""
class Solution(object):
    def mySqrt(self, x):
        """
        二分查找：
        x ** 2 - y = 0 =>
        """
        if x<=0:return 0
        if x==1:return 1
        low = 0
        high = x
        while( low < high ):
            mid = ( low + high ) / 2
            if( mid ** 2 < x and (mid+1)**2 > x or mid ** 2 == x):
                return mid
            if( mid ** 2 < x ):
                low = mid
            if( mid ** 2 > x ):
                high = mid


# print Solution().mySqrt( 3 )
# print Solution().mySqrt( 4 )
# print Solution().mySqrt( 1 )
