import pandas as pd


def nd(inPath,outPath):
    train_x = pd.read_csv(inPath)
    for i in range(1,11,1):
        train_x['n'+str(i)] = (train_x == i).sum(axis=1)
    train_x[['uid','n1','n2','n3','n4','n5','n6','n7','n8','n9','n10']].\
        to_csv(outPath,index=None)

browse_discretization_path = 'E:/data/browse_discretization.csv'
bill_discretization_path = 'E:/data/bill_discretization.csv'
bank_discretization_path = 'E:/data/bank_discretization.csv'


browse_num_path = 'E:/data/browse_nd.csv'
bill_num_path = 'E:/data/bill_nd.csv'
bank_num_path = 'E:/data/bank_nd.csv'

nd(browse_discretization_path,browse_num_path)
nd(bill_discretization_path,bill_num_path)
nd(bank_discretization_path,bank_num_path)



