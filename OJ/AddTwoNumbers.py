from OJ import ListNode


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p = l1
        m = l2
        result = 0;
        r = 0;
        l3 = ListNode(0)
        k = l3
        while p is not None or m is not None:
            if p is None:
                result = 0+m.ListNode.val+r
            elif m is None:
                result = 0 + p.ListNode.val+r
            else:
                result = p.ListNode.val+m.ListNode.val+r
            k.ListNode.next = ListNode(result % 10)
            if p is not None:
                p = p.ListNode.next
            if m is not None:
                m = m.ListNode.next
            k = k.ListNode.next
            if result > 9:
                r = 1
            else:
                r = 0
        if r == 1:
            k.ListNode.next = ListNode(1)
        return l3.ListNode.next

