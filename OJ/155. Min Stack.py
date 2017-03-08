# coding=utf-8
__author__ = 'arachis'
"""
Design a _stack that supports push, pop, top, and retrieving the minimum element in constant time.
设计一个支持push,pop,top和getMin()操作的栈，getMin()要求O(1)时间的
"""
class MinStack(object):

    def __init__(self):
        self._stack = []

    def push(self, x):#栈的元素类型是（e,min）,其中min是当前栈内的最小值
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self._stack.append((x, curMin))

    def pop(self):
        self._stack.pop()

    def top(self):
        if len(self._stack) == 0:
            return None
        else:
            return self._stack[len(self._stack) - 1][0]

    def getMin(self):
        if len(self._stack) == 0:
            return None
        else:
            return self._stack[len(self._stack) - 1][1]


# Your Min_stack object will be instantiated and called as such:
# obj = Min_stack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()