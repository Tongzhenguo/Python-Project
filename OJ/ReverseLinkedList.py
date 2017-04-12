# coding=utf-8
from datastructure.ListNode import ListNode

__author__ = 'arachis'

class Solution(object):
    def reverseList(self, head):
        if head == None or head.next == None:
            return head
        pre = head
        cur = head.next
        while(cur != None):
            pre.next = cur.next #保存后面的节点
            cur.next = head #
            head = cur#更新头节点
            cur = pre.next#更新移动节点
        return head

if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)

    n1.next = n2
    n2.next = n3
    reverse_list = Solution().reverseList(n1)
    l = reverse_list
    while(l != None):
        print(l.val)
        l = l.next