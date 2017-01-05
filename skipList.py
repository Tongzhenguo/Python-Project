# coding=utf-8
"""
    跳表（skip list）
        原理：http://blog.sina.com.cn/s/blog_72995dcc01017w1t.html
        实现代码：http://www.cnblogs.com/wuditju/p/5995957.html
"""
import random

# 最高层数设置为4
MAX_LEVEL = 4

def randomLevel():
    """
    相当与做一次丢硬币的实验，如果遇到正面，继续丢，遇到反面，则停止
    :return: random level
    """
    k = 1
    while random.randint(1, 100) % 2:
        k += 1
    k = k if k < MAX_LEVEL else MAX_LEVEL
    return k


def traversal(skiplist):
    """
    跳表的遍历功能
    对每一层的元素都进行遍历
    :param skiplist: 待遍历的跳表
    :return: None
    """
    level = skiplist.level
    i = level - 1
    while i >= 0:
        level_str = 'header'
        header = skiplist.header
        while header:
            level_str += ' -> %s' % header.key
            header = header.forward[i]
        print level_str
        i -= 1


class Node(object):
    def __init__(self, level, key, value):
        """
        跳表节点初始化
        :param level: 这个节点在小于等于level的层数都出现了
        :param key: 查询关键字
        :param value: 存储的信息
        """
        self.key = key
        self.value = value
        self.forward = [None] * level


class Skiplist(object):
    def __init__(self):
        """
        跳表初始化 层数为0 初始化头部节点()
        """
        self.level = 0
        self.header = Node(MAX_LEVEL, 0, 0)

    def insert(self, key, value):
        """
       先确定该元素要占据的层数 K（采用丢硬币的方式，这完全是随机的）,randomLevel()
       然后在 Level 1 ... Level K 各个层的链表都插入元素。
        :return: Boolean 用于判断插入成功或失败
        """
        # 更新的最大层数为 MAX_LEVEL 层
        update = [None] * MAX_LEVEL
        p = self.header
        q = None
        k = self.level
        i = k - 1
        # i from k-1 to 0
        while i >= 0:
            q = p.forward[i]
            while q and q.key < key:
                p = q
                q = p.forward[i]
            update[i] = p
            i -= 1
        if q and q.key == key:
            return False

        k = randomLevel()
        if k > self.level:
            i = self.level
            while i < k:
                update[i] = self.header
                i += 1
            self.level = k

        q = Node(k, key, value)
        i = 0
        while i < k:
            q.forward[i] = update[i].forward[i]
            update[i].forward[i] = q
            i += 1
        return True

    def delete(self, key):
        """
        首先找到我们要删除节点的位置，在查找时使用临时空间记录节点在每一级的位置。
        接着就是逐层的链表删除操作。
        最后记住要释放空间。
        删除节点之后，如果最高层没有节点存在，那Skip List的层数相应的需要降下来。
        :return: Boolean 用于判断删除成功或失败
        """
        update = [None] * MAX_LEVEL
        p = self.header
        q = None
        k = self.level
        i = k - 1
        while i >= 0:# 跟插入一样 找到要删除的位置
            q = p.forward[i]
            while q and q.key < key:
                p = q
                q = p.forward[i]
            update[i] = p
            i -= 1
        if q and q.key == key:
            i = 0
            while i < self.level:
                if update[i].forward[i] == q:
                    update[i].forward[i] = q.forward[i]
                i += 1
            del q
            i = self.level - 1
            while i >= 0:
                if not self.header.forward[i]:
                    self.level -= 1
                i -= 1
            return True
        else:
            return False

    def search(self, key):
        """
        跳表搜索操作
        :return: 节点的 key & value & 节点所在的层数(最高的层数)
        """
        i = self.level - 1
        while i >= 0:
            q = self.header.forward[i]
            while q and q.key <= key:
                if q.key == key:
                    return q.key, q.value, i
                q = q.forward[i]
            i -= 1
        return None

if __name__ == '__main__':
    number_list = (7, 4, 1, 8, 5, 2, 9, 6, 3)
    skiplist = Skiplist()
    for number in number_list:
        skiplist.insert(number, None)

    traversal(skiplist)
    print skiplist.search(4)
    skiplist.delete(4)
    traversal(skiplist)
