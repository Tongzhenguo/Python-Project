# coding=utf-8
import collections

__author__ = 'arachis'
"""
Implement the following operations of a queue using stacks.
使用栈操作实现队列的基本操作，尤其是push(x)和pop()
push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Notes:
You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
"""
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._queue = collections.deque()

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        tmp = collections.deque()
        while( not self.empty() ):
            tmp.appendleft( self._queue.popleft() ) #把栈中的全部元素弹出
        self._queue.append( x )#把新元素入栈
        while( len(tmp) > 0 ): #原来的元素反序入栈
            self._queue.appendleft( tmp.popleft() )

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self._queue.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self._queue : return None
        return self._queue[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len( self._queue ) == 0



# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
# param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
print param_3