# coding=utf-8

from __future__ import print_function


def PersonalRank(G, alpha, root, max_step):
    rank = {x: 0 for x in G.keys()}
    rank[root] = 1
    # 开始迭代
    for k in range(max_step):
        tmp = {x: 0 for x in G.keys()}
        # 取节点i和它的出边尾节点集合ri
        for i, ri in G.items():
            # 取节点i的出边的尾节点j以及边E(i,j)的权重wij, 边的权重都为1，在这不起实际作用
            for j, wij in ri.items():
                # i是j的其中一条入边的首节点，因此需要遍历图找到j的入边的首节点，
                # 这个遍历过程就是此处的2层for循环，一次遍历就是一次游走
                tmp[j] += alpha * rank[i] / (1.0 * len(ri))
                # 我们每次游走都是从root节点出发，因此root节点的权重需要加上(1 - alpha)
        # 在《推荐系统实践》上，作者把这一句放在for j, wij in ri.items()这个循环下，我认为是有问题。
        tmp[root] += (1 - alpha)
        rank = tmp

        # 输出每次迭代后各个节点的权重
        print('iter: ' + str(k) + "\t")
        for key, value in rank.items():
            print( "%s:%.3f, \t" % (key, value) )
        print()

    return rank


if __name__ == '__main__':
    G = {'A': {'a': 1, 'c': 1},
         'B': {'a': 1, 'b': 1, 'c': 1, 'd': 1},
         'C': {'c': 1, 'd': 1},
         'a': {'A': 1, 'B': 1},
         'b': {'B': 1},
         'c': {'A': 1, 'B': 1, 'C': 1},
         'd': {'B': 1, 'C': 1}}

    PersonalRank(G, 0.85, 'A', 100)