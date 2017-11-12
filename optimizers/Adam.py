# coding=utf-8
# Adam。
def adam(params, vs, sqrs, lr, batch_size, t):
    beta1 = 0.9
    beta2 = 0.999
    eps_stable = 1e-8
    for param, v, sqr in zip(params, vs, sqrs):
        g = param.grad / batch_size
        v[:] = beta1 * v + (1. - beta1) * g
        sqr[:] = beta2 * sqr + (1. - beta2) * nd.square(g)
        v_bias_corr = v / (1. - beta1 ** t)
        sqr_bias_corr = sqr / (1. - beta2 ** t)
        div = lr * v_bias_corr / (nd.sqrt(sqr_bias_corr) + eps_stable)
        param[:] = param - div

if __name__ == '__main__':
    import random
    import numpy as nd
    random.seed(1)

    # 生成数据集。
    num_inputs = 2
    num_examples = 1000
    true_w = [2, -3.4]
    true_b = 4.2
    X = nd.random_normal(scale=1, shape=(num_examples, num_inputs))
    y = true_w[0] * X[:, 0] + true_w[1] * X[:, 1] + true_b
    y += .01 * nd.random_normal(scale=1, shape=y.shape)
    dataset = gluon.data.ArrayDataset(X, y)

    # 构造迭代器。
    import random


    def data_iter(batch_size):
        idx = list(range(num_examples))
        random.shuffle(idx)
        for batch_i, i in enumerate(range(0, num_examples, batch_size)):
            j = nd.array(idx[i: min(i + batch_size, num_examples)])
            yield batch_i, X.take(j), y.take(j)


    # 初始化模型参数。
    def init_params():
        w = nd.random_normal(scale=1, shape=(num_inputs, 1))
        b = nd.zeros(shape=(1,))
        params = [w, b]
        vs = []
        sqrs = []
        for param in params:
            param.attach_grad()
            # 把算法中基于指数加权移动平均的变量初始化为和参数形状相同的零张量。
            vs.append(param.zeros_like())
            sqrs.append(param.zeros_like())
        return params, vs, sqrs


    # 线性回归模型。
    def net(X, w, b):
        return nd.dot(X, w) + b


    # 损失函数。
    def square_loss(yhat, y):
        return (yhat - y.reshape(yhat.shape)) ** 2 / 2