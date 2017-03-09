# coding=utf-8
__author__ = 'arachis'
"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
Follow up: Could you solve it without loops/recursion?
判断一个32位有符号整数是否是4的幂，近一步的，你的算法中是否可以不用循环或者递归
"""

"""
1
100
10000
1000000
得出4的幂是隔一个0产生一个1

先保证是2的幂，也即最高位是1，低位全为0；num & (num-1) == 0
然后再挑选出是4的幂，每隔2个0，产生一个1，为了把这些1保存，可以通过异或或者或运算
将int32内所有的4的幂(异)或，得到1010101010101010101010101010101 (1431655765)
如果是4的幂，那么相与结果还是本身。
可以看做是掩码，通过相与后可以得到想要的位，这里通过判断是2的幂，已经保证除了最高位其余位都是0了
"""
class Solution(object):
    def isPowerOfFour(self, num):
        if num < 1: return False #二进制转十进制
        return num & (num-1) == 0 and num & int( '1010101010101010101010101010101',2 ) == num

        # """
        # logN
        # """
        # if num < 1: return False
        # n = 1
        # array = []
        # while( n < (2 ** 31)-1 ):
        #     array.append( n )
        #     n *= 4
        # print array
        # i = 0
        # while( i< len(array) ):
        #     if num == array[i]:
        #         return True
        #     i += 1
        # return False

# print Solution().isPowerOfFour( 1 )
# print Solution().isPowerOfFour( -1 )
# print Solution().isPowerOfFour( 16 )
# print Solution().isPowerOfFour( 1162261466 )
