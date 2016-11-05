# coding=utf-8
"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
Examples:
s = "leetcode"
return 0.
s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
简单的说就是找到一个不重复字母的下标
"""


class Solution(object):
    def firstUniqChar(self, s):
        """我的想法就是两头同时遍历，当集合中不存在则返回，或者遍历完没找到
        :type s: str
        :rtype: int
        """
        i = 0
        dict = {}  ## char and index ,to save unique char key
        chars = list(s.lower())
        while (i < len(chars)):
            if (dict.has_key(chars[i])):
                dict.pop(chars[i])
            else:
                dict[chars[i]] = i
            i += 1
        if (len(dict) == 0):
            return -1
        else:
            return sorted(dict.values())[0]  ## min and becasue dict not make sure sorted append


print Solution().firstUniqChar("leetcode")
