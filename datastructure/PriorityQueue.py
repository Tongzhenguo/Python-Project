# coding=utf-8
"""
python 中的优先级队列
"""
from Queue import PriorityQueue
queue = PriorityQueue()
queue.put((16,'Suzuka'))
queue.put((15,'Moa'))
queue.put((14,'Yui'))
queue.put((17,'Ayaka'))
print queue.get()
