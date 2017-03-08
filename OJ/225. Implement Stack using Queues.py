# coding=utf-8
import collections

__author__ = 'arachis'
"""
Implement the following operations of a stack using queues.
使用队列实现栈的push(x)，pop()，top()，empty()操作
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
注：只能使用队列的标准操作实现，也就是说只能向队列末尾添加元素，从队首移除元素和返回队列的大小，以及判空方法
如果实现的语言没有队列这一数据结构，可以使用list模拟（simulate）队列。并且假定所有的操作都是合法，即不用判定空表不能pop,队列满不能插入
Notes:
You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue),
as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
"""
class MyStack(object):

    def __init__(self):
        self._queue = collections.deque()

    def push(self, x):#通过入到队尾，然后依次出对，入队
        q = self._queue
        q.append(x)
        for _ in range(len(q) - 1):
            q.append(q.popleft())

    def pop(self):
        return self._queue.popleft()

    def top(self):
        return self._queue[0]

    def empty(self):
        return not len(self._queue)
