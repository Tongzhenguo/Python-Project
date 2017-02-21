# coding=utf-8
from OJ.ListNode import ListNode

__author__ = 'arachis'

"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
归并两个有序链表，新链表长度是前两个的长度和
"""

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        """
        p,q = l1,l2
        if p==None and q==None:return None
        if p == None:return q
        if q == None:return p

        if( p.val <= q.val ):
            resLinkedList = ListNode(p.val)
            p = p.next
        else:
            resLinkedList = ListNode(q.val)
            q = q.next
        k = resLinkedList
        while( p != None and q != None ):
            if( p == None ): #一个遍历完就追加另一个链表
                p = q
            if( q == None ):
                q = p
            if( p.val <= q.val ):
                k.next = ListNode(p.val)
                p = p.next
            else:
                k.next = ListNode(q.val)
                q = q.next
            k = k.next
        if p == None:
            k.next = q
        if q == None:
            k.next = p
        return  resLinkedList

l1 = ListNode(1)
l2 = ListNode(1)
l3 = ListNode(2)

l4 = ListNode(1)
l5 = ListNode(4)
l1.next = l2
l2.next = l3

l4.next = l5
head = Solution().mergeTwoLists(l1, l4)
while( head!=None ):
    print head.val
    head = head.next
