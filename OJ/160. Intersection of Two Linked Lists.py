# coding=utf-8
from OJ.ListNode import ListNode

__author__ = 'arachis'

"""
Write a program to find the node at which the intersection of two singly linked lists begins.
写一个算法，找到两个单链表的首个相交点

For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:
注：如果不存在交点，返回空。不能改变原来的链表；假定入口没有环。最好时间是O(N)，空间是O(1)
If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """

        """
        if headA and headB:
            A, B = headA, headB
            while A!=B:
                A = A.next if A else headB #到达了尾部，交换链表
                B = B.next if B else headA
            return A

# l1 = ListNode(1)
# l2 = ListNode(2)
# l3 = ListNode(3)
# l4 = ListNode(4)
# l1.next = l4
# l2.next = l3
# l3.next = l4
# print Solution().getIntersectionNode(l1,l2)
