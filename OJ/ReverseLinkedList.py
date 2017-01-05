from datastructure.ListNode import ListNode

__author__ = 'arachis'

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        p = head
        q = head.next
        while(q != None):
            p.next = q.next
            q.next = head
            head = q
            q = p.next
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