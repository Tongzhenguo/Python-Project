# encoding: utf-8


"""


@author: tongzhenguo



@time: 2019/4/6 下午9:56


@desc:


"""

import tensorflow as tf


def field_weighted_aware(inputs, scope=None,
                         name="FieldWeightedAware", reuse=None,
                         initializer=tf.glorot_normal_initializer(),
                         l2_reg=None):
    """ 实现特征域间两两配对的交叉项

    Params:
        inputs: shape为(None, field, embed)的tensor

    Returns:
        特征域之间两两交叉的结果, shape=(None, embed_dim)

    """

    with tf.variable_scope(scope, default_name=name, values=[inputs],
                           reuse=reuse) as scope_bn:
        num_fields = inputs.get_shape().as_list()[1]
        weight_field_aware = tf.get_variable("my_weight_field_aware"
                        ,shape=(int(num_fields * (num_fields - 1) / 2), 1)
                        ,initializer=initializer
                        ,regularizer=l2_reg)

        index_left = []
        index_right = []
        for i in range(num_fields):
            for j in range(i + 1, num_fields):
                index_left.append(i)
                index_right.append(j)

        embeddings_left = tf.gather(params=inputs, indices=index_left, axis=1)
        embeddings_right = tf.gather(params=inputs, indices=index_right, axis=1)
        embeddings_prod = tf.multiply(x=embeddings_left, y=embeddings_right)
        field_aware_embedding = tf.multiply(x=embeddings_prod, y=weight_field_aware)
        field_aware_embedding = tf.reduce_sum(field_aware_embedding, axis=1)

    return field_aware_embedding
