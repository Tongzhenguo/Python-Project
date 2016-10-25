class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        chars = list(ransomNote)
        i = 0
        while (i < len(chars) and magazine.__contains__(chars[i])):
            magazine = magazine.replace(chars[i], "", 1)
            i += 1
        return i == len(chars)
