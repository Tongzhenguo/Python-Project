# coding=utf-8
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ### 如果拿完后剩下四的倍数则胜
        ### rang(start,stop), 包含start,不含stop
        for i in range(1,4):
            if((n -i) % 4 == 0):
                return True
        return False
    for i in range(1,11):
        print canWinNim(object,i)
