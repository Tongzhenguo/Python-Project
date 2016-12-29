class Solution(object):
    def intersect(self, nums1, nums2):
        """ M+N
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1Counter = {}
        nums2Counter = {}
        res = []
        for i in nums1:
            if not nums1Counter.has_key(i):
                nums1Counter.setdefault(i,0)
            nums1Counter[i] += 1
        for i in nums2:
            if not nums2Counter.has_key(i):
                nums2Counter.setdefault(i, 0)
            nums2Counter[i] += 1
        for i in nums1Counter:
            if nums2Counter.has_key(i):
                res.extend([i]* min(nums1Counter[i],nums2Counter[i]) )
        return sorted(res)
print Solution().intersect([1,2,2,1],[1,2,2])