# coding=utf-8
"""
Given a linked list, determine if it has a cycle in it.
判断一个链表是否有环，最好不使用额外的空间
Follow up:
Can you solve it without using extra space?
"""
from OJ.ListNode import ListNode


class Solution(object):
    def hasCycle(self, head):
        """
        两个指针，一个快，一个慢，如果相遇就有环
        """
        if head is None or head.next is None:return False
        p = head.next.next
        q = head
        while( p!= None ):
            if( p == q ):
                return True
            elif( p.next == None ):
                return False
            else:
                p = p.next.next
                q = q.next
        return False
node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(1)
node1.next = node2
# node2.next = node3
print Solution().hasCycle(node1)


node1.next = node2
node2.next = node1
# node3.next = node1
print Solution().hasCycle(node1)