import pandas as pd
from sklearn import preprocessing

# We split trainfile into train and valid pretty early on
trainfile_orig = pd.read_csv('../walmart-input/train.csv')
trainfile = trainfile_orig.copy()
# print trainfile.head()

test_orig = pd.read_csv('../walmart-input/test.csv')
test = test_orig.copy()
# print test.head()

sub_orig = pd.read_csv('../walmart-input/sample_submission.csv')
sub = sub_orig.copy()

def chop_triptype(tt):
    return int(tt[9:])

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
# print(triptypestr_map)
# print(triptype_map)
trainfile.TripType.replace(triptype_map, inplace=True)

def preproc(df):
    # replace days of week
    en = preprocessing.LabelEncoder()
    en.fit(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    df["Weekday"] = en.transform(df["Weekday"])

    df["FinelineNumber"].fillna(-1)
    df["FinelineNumber"] += 1

    # there are nan's that need to get converted
    df["DepartmentDescription"].fillna("nan")

    if 'TripType' in df:
        enc = preprocessing.OneHotEncoder()
        df["TripTypeOneHot"] = enc.fit_transform(df.TripType.reshape(-1, 1))

preproc(trainfile)
trainfile.to_csv("train.csv")
preproc(test)
test.to_csv("test.csv")