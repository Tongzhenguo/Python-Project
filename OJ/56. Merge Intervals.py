# coding=utf-8
__author__ = 'arachis'
"""
Given a collection of intervals, merge all overlapping intervals.
给一间隔的集合，合并可达的间隔，如下：
For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
ust go through the intervals sorted by start coordinate and either combine the current interval with the previous one if they overlap,
or add it to the output by itself if they don't.
"""
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    """先排序，然后如果当前起始小于结果序列的当前结尾，就合并成一个；否则序列新加一个间隔
    """
    def merge(self, intervals):
        out = []
        for i in sorted(intervals, key=lambda i: i.start):
            if out!=None and i.start <= out[-1].end:
                out[-1].end = max(out[-1].end, i.end)
            else:
                out.append(i)
        return out