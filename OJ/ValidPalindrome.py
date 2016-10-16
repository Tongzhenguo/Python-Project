# coding=utf-8
class Solution(object):
    def isAlphanumeric(self,char):## lower
        return (char>='0' and char<='9') or (char>='a' and char<='z')
    def isPalindrome(self, s):
        """判断字符串是不是回文，只验证字母和数字
        :type s: str
        :rtype: bool
        """
        bytes = list(s.lower())
        left = 0
        right = len(bytes)-1
        while(left<right):
            if(self.isAlphanumeric(bytes[left]) and self.isAlphanumeric(bytes[right])):
                if(bytes[left] != bytes[right]):
                    return False
                else:
                    left+=1
                    right-=1
            if(not self.isAlphanumeric(bytes[left])):
                left+=1
            if(not self.isAlphanumeric(bytes[right])):
                right-=1
        return True
