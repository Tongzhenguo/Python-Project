__author__ = 'arachis'

import pandas as pd

loan = pd.read_csv("E:\Python-Project\dataset\loan.csv",delimiter="\\t")
features = loan.columns.tolist()
for feature in features:
    loan["new"+feature] = feature+":"+loan[loan.feature]