import pandas as pd
from sklearn import preprocessing

def chop_triptype(tt):
    return int(tt[9:])

def preproc(file):
    df = pd.read_csv(file)
    # replace days of week
    en = preprocessing.LabelEncoder()
    en.fit(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    df["Weekday"] = en.transform(df["Weekday"])

    df["FinelineNumber"] = df["FinelineNumber"].fillna(-1)
    df["FinelineNumber"] += 1
    df["FinelineNumber"] = df["FinelineNumber"].astype(int)

    # there are nan's that need to get converted
    df["DepartmentDescription"].fillna("nan")

    dden = preprocessing.LabelEncoder()
    dden.fit( df["DepartmentDescription"] )
    df['DepartmentDescription'] = dden.transform( df['DepartmentDescription'] )


    sub_orig = pd.read_csv('../walmart-input/sample_submission.csv')
    sub = sub_orig.copy()
    if 'TripType' in df:
        triptype_map = {}
        triptypestr_map = {}

        c = 0
        for k in sub.loc[0].keys():
            if 'TripType_' in k:
                triptypestr_map[k] = c
                triptype_map[chop_triptype(k)] = c
                c += 1
        # replace type 999 with 45 to keep from wasting memory in structs
        triptype_map[45] = triptype_map[999]
        df.TripType.replace(triptype_map, inplace=True)

        enc = preprocessing.OneHotEncoder()
        df["TripTypeOneHot"] = enc.fit_transform(df.TripType.reshape(-1, 1))

    return df
# print preproc('../walmart-input/test.csv').head(5)
# print preproc("../walmart-input/train.csv").head(5)