"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""

class Solution(object):
    def isMatch(self,c1,c2):
        return ("()"==""+c1+c2) or ("[]"==""+c1+c2) or ("{}"==""+c1+c2)
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = []
        for char in list(s):
            length = len(brackets)
            if(0 != length and self.isMatch(brackets[length-1],char)):
                brackets.pop()
            else:
                brackets.append(char)
        return 0 == len(brackets)
print Solution().isValid("{[)")
