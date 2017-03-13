# coding=utf-8
"""
Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.
十进制数转十六进制数，十六进制数中不用0填充，输入一般是int32类型，要求不能使用关于16进制转换的库函数
Note:

Example 1:
Input:
26
Output:
"1a"

Example 2:
Input:
-1
Output:
"ffffffff"
"""
class Solution(object):
    def toHex(self, num):
        """
        先都看作是非负数，然后负数要转成补数（2 ** 32 + n）
        """
        if num == 0: return '0'
        s = ''
        hexHash = [] #keep a map decimal to hex
        for i in range(16):
            if i>=10:
                hexHash.append(chr(97+i-10))
            else:
                hexHash.append(str(i))
        n = num if num > 0 else 2 ** 32 + num #-1 => 2 ** 32 - 1
        i = 0
        while (n > 0):
            s = hexHash[ n % 16 ] + s
            n = n >> 4
            i += 1
        return s

print Solution().toHex(26)
print Solution().toHex(-1)
