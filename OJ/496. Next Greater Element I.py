# coding=utf-8
__author__ = 'arachis'
"""
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2.
Find all the next greater numbers for nums1's elements in the corresponding places of nums2.
The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2.
If it does not exist, output -1 for this number.
输入有两个不重复的数组，nums1和nums2，其中nums2是nums1的子集，
nums1中的下一个更大的数字x是nums2元素nums1[i]往右边的第一个更大的数字nums2[j],如果不存在,就是-1
例如：
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]

"""
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        Suppose we have a decreasing sequence followed by a greater number.
        For example [5, 4, 3, 2, 1, 6] then the greater number 6 is the next greater element for all previous numbers in the sequence.
        We use a stack to keep a decreasing sub-sequence, whenever we see a number x greater than stack.peek()
        we pop all elements less than x and for all the popped ones, their next greater element is x.For example [9, 8, 7, 3, 2, 1, 6].
        The stack will first contain [9, 8, 7, 3, 2, 1] and then we see 6 which is greater than 1 so we pop 1 2 3 whose next greater element should be 6.
        """
        cache, st = {}, [] #出栈的元素，维护一个降序的栈
        for x in nums:
            while len(st) > 0 and st[-1] < x:#比栈顶中最小的元素大
                cache[st.pop()] = x
            st.append(x)
        result = [-1 for e in findNums ]
        for idx,x in enumerate(findNums):
            if x in cache:
                result[idx] = cache[x]
        return result

# print Solution().nextGreaterElement( [4,1,2],[1,3,4,2] )