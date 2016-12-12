import pandas as pd

def n_null(inPath,outPath):
    train_x = pd.read_csv(inPath)
    train_x['n_null'] = (train_x == 0).sum(axis=1)
    # train_x[["n_null"]].describe()
    train_x['discret_null'] = train_x.n_null
    steps = train_x[["n_null"]].describe().values[3:]
    train_x.discret_null[train_x.discret_null<=steps[0,0]] = 1
    for i in range(len(steps)-1):
      train_x.discret_null[(train_x.discret_null>steps[i,0]) & (train_x.discret_null<=steps[i+1,0])] = i+2
    return train_x[['uid','n_null','discret_null']].to_csv(outPath,index=None)


merge_path = "E:/data/merge.csv"
merge_null_path = "E:/data/merge_null.csv"
res = n_null(merge_path, merge_null_path)


