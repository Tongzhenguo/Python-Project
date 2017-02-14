# coding=utf-8
__author__ = 'arachis'

"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
给一个字符串数组，找到可以用美式键盘中同一行的字母组合敲出来的字符串
Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
可以多次使用同一个字母，并且假定字符串都是由字母组成
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
"""
class Solution(object):
    def findWords(self, words):
        """
        """
        keyMap = {
                'q':0,'w':0,'e':0,'r':0,'t':0,'y':0,'u':0,'i':0,'o':0,'p':0,
                'a':1,'s':1,'d':1,'f':1,'g':1,'h':1,'j':1,'k':1,'l':1,
                'z':2,'x':2,'c':2,'v':2,'b':2,'n':2,'m':2
                  }
        res = []
        for word in words:
            ss = list(word.lower())
            rank = keyMap[ ss[0] ]
            flag = True
            for a in ss:
                if( rank != keyMap[a] ):
                    flag = False
                    break
            if(flag):
                res.append( word )
        return res
print Solution().findWords(["Hello", "Alaska", "Dad", "Peace"])