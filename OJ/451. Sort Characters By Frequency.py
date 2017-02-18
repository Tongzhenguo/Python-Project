# coding=utf-8
"""
Given a string, sort it in decreasing order based on the frequency of characters.
根据字符出现的次数对字符串排序
"""

class Solution(object):
    def frequencySort(self, s):
        fdict = {}
        sList = list(s)
        tList = []
        for c in sList:
            fdict[c] = fdict.get(c,0) + 1
        sorted1 = sorted(fdict.iteritems(), key=lambda p: p[1], reverse=True)
        for item in sorted1:
            tList.extend( list(item[0])*item[1] )
        return "".join(tList)
# Solution().frequencySort("1233")