# coding=utf-8
from OJ.ListNode import ListNode

__author__ = 'arachis'
"""
Given a singly linked list, determine if it is a palindrome.
判断单链表是不是回文，时间 O(n)，空间O(1)
Follow up:
Could you do it in O(n) time and O(1) space?
"""

class Solution(object):
    def isPalindrome(self, head):
        """
        Reverse the first half of the linked list and compare it to the second half.
        """
        count = 0
        node = head
        while node:
            node = node.next
            count += 1
        node = head
        pre = None
        for i in range(count / 2):
            temp = node.next #反转
            node.next = pre
            pre = node
            node = temp
        if count % 2 == 0:
            h2 = node #后一半
        else:
            h2 = node.next
        h1 = pre #前一半
        while h1:
            if h1.val == h2.val:
                h1 = h1.next
                h2 = h2.next
            else:
                return False
        return True

l1 = ListNode(1)
l2 = ListNode(1)
l3 = ListNode(1)

l4 = ListNode(1)
l5 = ListNode(4)
l1.next = l2
l2.next = l3

l4.next = l5
print Solution().isPalindrome(l1)
# while( head!=None ):
#     print head.val
#     head = head.next


