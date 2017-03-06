# coding=utf-8
__author__ = 'arachis'
"""
You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check.
Since each version is developed based on the previous version, all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which will return whether version is bad.
Implement a function to find the first bad version. You should minimize the number of calls to the API.
产品的版本之间是有依赖的，如果当前版本有问题，下一个版本也会有问题。给你一个方法：bool isBadVersion(version)，
"""
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    pass
class Solution(object):
    def firstBadVersion(self, n):
        if isBadVersion(1):return 1
        low = 2
        high = n
        while( low <= high ):
            mid = ( low + high ) / 2
            if( isBadVersion(mid) and  not isBadVersion(mid-1) ):
                return mid
            elif( isBadVersion(mid) and  isBadVersion(mid-1) ):
                high = mid-1
            else:
                low = mid+1

# print Solution().firstBadVersion( 1 )
# print Solution().firstBadVersion( n )
# print Solution().firstBadVersion( n-2 )
# print Solution().firstBadVersion( 1 )