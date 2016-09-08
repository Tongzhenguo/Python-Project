import random
import math


def stocGradDescent(self) :
        """
        计算权重系数向量
        """
        m, n = weiCount(self.train_vec_list)
        for j in range(10):
            dataIndex = range(m)#生成一个长度为1500左右的list
            for index in range(m) :
                alpha = 4 / (1.0 + j + index) + 0.01
                randIndex = int(random.uniform(0, len(dataIndex)))
                h = sigmoid(sumArray(self.train_vec_list[randIndex], self.weights))
                #print "h:",h,
                error = self.class_list[randIndex] - h
                #print "error", error,
                self.weights = arraySub(self.weights, arrayMulti(alpha, error, self.train_vec_list[randIndex]))
                del(dataIndex[randIndex])
def sigmoid(vecX) :
    return 1.0 / (1 + math.exp(-vecX))

def weiCount(data_mat) :
#返回train_vec_list行数和列数
    return len(data_mat), len(data_mat[0])
def sumArray(lineVec, weights) :
    #两向量的内积
    total = 0
    for index in range(len(lineVec)) :
        total += (lineVec[index] * weights[index])
    #print "total:", total,
    return total
def arrayMulti(count, error, lineVec) :
    for index in range(len(lineVec)) :
        lineVec[index] = count * error * lineVec[index]
    return  lineVec
def arraySub(weights, lineVec) :
    for index in range(len(weights)) :
        weights[index] = weights[index] + lineVec[index]
    return weights