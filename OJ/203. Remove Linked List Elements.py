# coding=utf-8
from OJ.ListNode import ListNode

__author__ = 'arachis'

"""
Remove all elements from a linked list of integers that have value val.
去除单链表指定数值
Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5

"""

class Solution:
    def getIntersectionNode(self, headA, headB):
        """
        the idea is if you switch head, the possible difference between length would be countered.
        On the second traversal, they either hit or miss.
        if they meet, pa or pb would be the node we are looking for,
        if they didn't meet, they will hit the end at the same iteration, pa == pb == None, return either one of them is the same,None
        """
        if headA is None or headB is None:
            return None

        pa = headA # 2 pointers
        pb = headB

        while pa != pb:
            #  if either pointer hits the end, switch head and continue the second traversal,
            # if not hit the end, just move on to next
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        return pa # only 2 ways to get out of the loop, they meet or the both hit the end=None



# l1 = ListNode(1)
# l2 = ListNode(2)
# l3 = ListNode(2)
# l4 = ListNode(4)
# l1.next = l2
# l2.next = l3
# l3.next = l4
# head = Solution().removeElements(l1, 1)
# while( head != None ):
#     print head.val
#     head = head.next
