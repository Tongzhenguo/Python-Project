# encoding: utf-8


"""

@author: tongzhenguo
@time: 2019/6/5 下午12:10
@desc:
原文：https://blog.csdn.net/xiadimichen14908/article/details/83592282

"""

import tensorflow as tf

# TensorFlow控制语句
# tf.cond(
# pred,
# true_fn=None,
# false_fn=None,...
# )
# 官网描述
# 当pred=True的时候返回true_fn()，pred=False的时候返回false_fn().

# state=tf.Variable(0)
# one=tf.constant(1)
# new_value=tf.add(state,one)
# update=tf.assign(state,new_value)
# init=tf.initialize_all_variables()
# cond=tf.cond(tf.greater_equal(new_value,2),lambda:update,lambda:tf.constant(-1))
# with tf.Session() as sess:
#     sess.run(init)
#     for _ in range(3):
#         print("new_value",new_value.eval())
#         print(sess.run(cond))


# tf.where(
# condition,
# x=None,
# y=None,
# name=None
# )
# 官网描述
# 根据conditioin的值要么返回x要么返回y中元素。
# 如果x,y都为None那么返回condition中true元素的坐标

# arr=tf.constant([[-1,0,1,2],
#                 [2,0,-3,-5]])
# pred=tf.less(arr,0)
# ans=tf.where(pred)
# with tf.Session() as sess:
#     sess.run(tf.initialize_all_variables())
#     print("pred is")
#     print(sess.run(pred))
#     print("tf.where")
#     print(sess.run(ans))

# arr=tf.constant([[-1,0,1,2],
#                 [2,0,-3,-5]],tf.float32)
# pred=tf.less(arr,0)
# ans=tf.where(pred,arr,tf.zeros([2,4],tf.float32))
# with tf.Session() as sess:
#     sess.run(tf.initialize_all_variables())
#     print("pred is")
#     print(sess.run(pred))
#     print("tf.where")
#     print(sess.run(ans))


# 按照indice从params整合slice
# tf.gather(
# params,
# indices,
# validate_indices=None,
# name=None,
# axis=0
# )
