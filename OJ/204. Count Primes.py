# coding=utf-8
import math

__author__ = 'arachis'

"""
Count the number of prime numbers less than a non-negative number, n.
统计小于n的素数的个数，n>=0
"""

class Solution(object):
    def countPrimes(self, n):
        if n <= 2:return 0
        cn = 0
        notPrime = [False for i in range(n)]  #init 素数
        for i in range(2,n,1):
            if( not notPrime[i] ):
                cn += 1
                j = 2
                while( i*j < n ): #能由i>=2,j>=2表示，不是素数
                    notPrime[ i*j ] = True
                    j += 1
        return cn
print Solution().countPrimes(0)
print Solution().countPrimes(2)
print Solution().countPrimes(5)
print Solution().countPrimes(10)
