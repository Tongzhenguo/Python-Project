# coding=utf-8
"""
蓄水池抽样算法：
    从S中抽取首k项放入「水塘」中
    对于每一个S[i]项（i ≥ k）：
        随机产生一个范围0到i的整数r
        若 r < k 则把水塘中的第r项换成S[i]项
"""
from random import *

def reservoir_sampling(A, k):
    sample = []
    for i, a in enumerate(A):
        if i < k:  # 生成k大小的水塘
            sample.append(a)
        else:  # 递减概率随机替换水塘内元素
            r = randint(0, i)
            if r < k:
                sample[r] = a
    return sample

### this is a test for  reservoir_sampling
# A = [1,2,3,4,5,6,7,8,9]
# print reservoir_sampling(A,5)


