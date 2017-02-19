# coding=utf-8
"""
Given a sorted linked list, delete all duplicates such that each element appear only once.
删除一个有序链表的所有重复节点
For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""
from OJ.ListNode import ListNode

class Solution(object):
    def deleteDuplicates(self, head):
        """
        遍历，记录上一个值和当前值，如果相同就跳过
        直到找到不同的值，指向
        """
        if head is None:return head
        p = head.next
        q = head
        k = head
        while (p != None and p.val == q.val):
            q = p
            p = p.next
        k.next = p #遍历完或者第一个不同值出现
        while( p !=  None ):
            if( p.val != q.val ):
                k.next = p
                k = k.next
            q = p
            p = p.next
        k.next = None #去掉后面相同的
        return head

# node1 = ListNode(1)
# node2 = ListNode(2)
# node3 = ListNode(2)
# node1.next = node2
# node2.next = node3
#
# head =  Solution().deleteDuplicates(node1)
# while( head != None ):
#     print head.val
#     head = head.next