# coding=utf-8
import csv
import sys

import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix

# sys.path.append("/home/sudalai/Softwares/xgboost-master/wrapper/")
# sys.path.append("/home/sudalai/Softwares/XGB_pointfour/xgboost-master/wrapper/")
import xgboost as xgb


def multiclassLogLoss(y_true, y_pred, eps=1e-15):
    """Multi class version of Logarithmic Loss metric.
    https://www.kaggle.com/wiki/MultiClassLogLoss

    Parameters
    ----------
    y_true : array, shape = [n_samples]
            true class, intergers in [0, n_classes - 1)
    y_pred : array, shape = [n_samples, n_classes]

    Returns
    -------
    loss : float
    """
    predictions = np.clip(y_pred, eps, 1 - eps)

    # normalize row sums to 1
    predictions /= predictions.sum(axis=1)[:, np.newaxis]

    actual = np.zeros(y_pred.shape)
    n_samples = actual.shape[0]
    actual[np.arange(n_samples), y_true.astype(int)] = 1
    vectsum = np.sum(actual * np.log(predictions))
    loss = -1.0 / n_samples * vectsum
    return loss

#训练集和测试集转成稀疏矩阵形式
def getData(file_name):
    reader = csv.reader(open(file_name))
    header = reader.next()

    row_list = []
    col_list = []
    data_list = []
    row_ind = 0
    for row in reader:
        row = map(int, row)
        for col_ind, col_val in enumerate(row):
            if col_val != 0:
                row_list.append(row_ind)
                col_list.append(col_ind)
                data_list.append(col_val)
        row_ind += 1
        if(row_ind %1000 == 0):
            print row_ind
    sp_array = csr_matrix((data_list, (row_list, col_list)), shape=(row_ind, len(header)))

    return sp_array


def getTestData(file_name):
    reader = csv.reader(open(file_name))
    header = reader.next()

    row_list = []
    col_list = []
    data_list = []
    row_ind = 0
    for row in reader:
        row = map(int, row)
        for col_ind, col_val in enumerate(row):
            if col_val != 0:
                row_list.append(row_ind)
                col_list.append(col_ind)
                data_list.append(col_val)
        row_ind += 1
        if(row_ind %1000 == 0):
            print row_ind
    sp_array = csr_matrix((data_list, (row_list, col_list)), shape=(row_ind, len(header)))

    return sp_array


def runXGB(train_X, train_y):
    xg_train = xgb.DMatrix(train_X, label=train_y)

    ## Setting up the params ##
    param = {}
    # use softmax multi-class classification
    param['objective'] = 'multi:softprob'
    # scale weight of positive examples
    param['eta'] = 0.05  #衰减因子，学习步长/速率
    param['max_depth'] = 6
    param['silent'] = 0
    param['num_class'] = 38
    param['eval_metric'] = "mlogloss"
    # param['min_child_weight'] = 2
    param['subsample'] = 0.9
    param['colsample_bytree'] = 0.7
    param['gamma'] = 1  #最小损失函数

    # watchlist = [ (xg_train,'train'), (xg_test, 'test') ]
    num_round = 1000
    bst = xgb.train(param, xg_train, num_round)
    return bst


if __name__ == "__main__":
    # setting the input path and reading the data into dataframe #
    print "Reading data.."
    data_path = "E:\Python-Project\dataminingcontest\kaggle\Walmart_TripType_Classification\walmart-input"
    train_X = getData(data_path + "train_mod_v5.csv")
    train_y = np.array(pd.read_csv(data_path + "train_mod_v5_dv.csv")["DV"])
    print "Train shape : ", train_X.shape

    bst = runXGB(train_X, train_y)
    del train_X
    del train_y
    import gc

    gc.collect()

    print "Working on test.."
    test_X = getTestData(data_path + "test_mod_v5.csv")
    test_id = np.array(pd.read_csv(data_path + "test_mod_v7.csv", usecols=["VisitNumber"])["VisitNumber"])
    print test_X.shape
    xg_test = xgb.DMatrix(test_X)
    preds = bst.predict(xg_test)  # .reshape( test_X.shape[0], param['num_class'] )

    sample = pd.read_csv(data_path + "sample_submission.csv")
    preds = pd.DataFrame(preds, index=test_id, columns=sample.columns[1:])
    preds.to_csv("sub6.csv", index_label="VisitNumber")
