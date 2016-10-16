# coding=utf-8
class Solution(object):
    def fizzBuzz(self, n):
        """判断是3,5的倍数
        :type n: int
        :rtype: List[str]
        """
        strList = []
        for i in range(1,n+1):
            tmpStr = ""
            if(i%3==0):
                tmpStr += "Fizz"
            if(i%5==0):
                tmpStr += "Buzz"
            if(i%3!=0 and i%5!=0):
                tmpStr += str(i)
            strList.append(tmpStr)
        return strList
    print fizzBuzz(object,15)