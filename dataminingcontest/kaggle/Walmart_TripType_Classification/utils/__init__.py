import numpy as np
# sub_orig = pd.read_csv('walmart-input/sample_submission.csv')
# sub = sub_orig.copy()
from sklearn import preprocessing


def train_valid_split(trainfile):
    # Now split the train data into train+valid.
    #  2.5% with seed 0 appears to be pretty good, at least until this gets competitive
    visits = np.unique(trainfile.VisitNumber)

    # determine visits to go in validation set
    np.random.seed(0)
    validation_visits = np.random.choice(visits, int(len(visits) * .025))
    validation_set = (trainfile.VisitNumber == validation_visits[0])

    for i in range(1, len(validation_visits)):
        validation_set |= trainfile.VisitNumber == validation_visits[i]
    valid = trainfile.ix[validation_set]

    # flip that around to get the train set
    training_set = np.invert(validation_set)
    train = trainfile.ix[training_set]
    return  (train,valid)

def build_visitmaps(df):
    visits = np.unique(df.VisitNumber)
    visitmap = {}
    vtype = np.zeros(len(visits))

    if 'TripType' in df:
        for i in range(len(visits)):
            vtype[i] = df.ix[df.VisitNumber == visits[i]].iloc[0].TripType

    for i in range(len(visits)):
        visitmap[visits[i]] = i

    return visits, vtype, visitmap

# valid_visits, valid_type, valid_visitmap = build_visitmaps(valid)
# test_visits, test_type, test_visitmap = build_visitmaps(test)

# build map
# ddmap = {}
# for i in range(len(ddcat)):
#     ddmap[ddcat[i]] = i

# apply map
def makeddint(df):
    ddcatout = np.zeros(len(df.DepartmentDescription))
    # make categorical #'s.  TODO: move up to preproc???
    ddcat = np.unique(train.DepartmentDescription)
    for i in range(len(ddcat)):
        ddcatout[np.where(df.DepartmentDescription == ddcat[i])] = i

    # XXX: this is raising a SettingWithCopyWarning on valid and possibly train
    df['DepartmentDescriptionInt'] = ddcatout.astype(int)
    return df

# train = makeddint(train)
# valid = makeddint(valid)
# test = makeddint(test)

Construct set of usable DepartmentDescriptionInt keys (with >1000 per dept)
train_psc = train[train.ScanCount >= 1]
vc = train_psc.DepartmentDescriptionInt.value_counts()

ddi_len = np.zeros(len(ddcat))
ddi_keys = {}

for i in vc.iteritems():
    ddi_len[i[0]] = i[1]

    if i[1] > 1000:
        ddi_keys[i[0]] = True

train_psc = train[train.ScanCount >= 1]
subsetted = np.full(len(train_psc), False, dtype=bool)

flmap = {}
flnd = {}
ddmax = np.max(train.DepartmentDescriptionInt) + 1
fnum = 6
# # 0 - % items returned
# # 1 - 1 item
# # 2 - 2 items
# # 3 - 3-4 items
# # 4 - 5-9 items
# # 5 - 10+ items
#
f_ddstart = 6
f_ddend = 6 + ddmax
#
# # 6-ddmax: coarse dept description
fnum += ddmax
#
# # rest of fnum: fineline mapping
for cat in range(0, ddmax):
    # for cat in [20]:
    catmask = train_psc.DepartmentDescriptionInt == cat
    subset = train_psc[catmask]
    # print(cat, len(subset))

    if len(subset) < 10:
        continue

    vc = subset.FinelineNumber.value_counts()

    for iterit in vc.iteritems():
        fln = iterit[0]
        if (iterit[1] < 10):  # or (len(subset) < (iterit[1] * 2)):
            continue
        fnum += 1
        flmap[(cat, fln)] = fnum

# print(len(flmap.keys()))
# for i in flmap:
#     print(i, flmap[i])


def make_ddcomb(df, num_visits=100000000):
    num_ents = len(df)
    visits = np.sort(np.unique(df.VisitNumber))
    num_visits = min(num_visits, len(visits))
    ddmax = np.max(train.DepartmentDescriptionInt)
    mat = np.zeros((num_visits, (ddmax * 1) + fnum + 2))
    tt = np.zeros(num_visits)
    df_scancount = df.ScanCount.values
    df_visitnumber = df.VisitNumber.values
    df_triptype = df.TripType.values if ('TripType' in df) else np.zeros(len(df))
    df_ddint = df.DepartmentDescriptionInt.values
    df_fln = df.Upc.values
    df_fln = df.FinelineNumber.values
    #    df_fmap = df.fmap.values
    df_weekday = df.Weekday.values
    visitmap = {}

    vnum = -1

    icount = np.zeros(num_visits + 1)

    for i in range(0, num_ents):
        try:
            visit = visitmap[df_visitnumber[i]]
        except:
            vnum += 1

            if (vnum + 1) == num_visits:
                break

            visitmap[df_visitnumber[i]] = vnum
            visit = vnum

            tt[vnum] = df_triptype[i]
        # mat[visit][fnum + 1] = df_weekday[i] >= 6
        #            mat[visit][fnum + 2] = df_weekday[i] == 1
        #            mat[visit][fnum + df_weekday[i]] = 1

        icount[visit] += 1

        if True:  # df_scancount[i] > 0:
            dept = df_ddint[i]
            fln = df_fln[i]

            # allocation space:
            # 0 - % returns
            # 1 - ddmax - regular map
            # ddmax - ddmax*2 - leftovers
            # ddmax*2 >= +fmap - map

            mat[visit][6 + df_ddint[i]] += (1 + ((df_scancount[i] - 1) * .25))

            try:
                feature = flmap[(dept, fln)]
                mat[visit][feature] += (1 + ((df_scancount[i] - 1) * .25))
            except:
                None
                # feature = 1 + ddmax + dept
                # mat[visit][feature] += (1 + ((df_scancount[i] - 1) * .25))

        if df_scancount[i] < 0:
            mat[visit][0] += 1

    vnum += 1
    for i in range(0, vnum):
        if np.sum(mat[i][f_ddstart:f_ddend]):
            #            mat[i][] /= np.sum(mat[i][f_ddstart:f_ddmax])
            mat[i][f_ddstart:f_ddend] /= np.sum(mat[i][f_ddstart:f_ddend])
        if np.sum(mat[i][f_ddend:fnum]):
            mat[i][f_ddend:fnum] /= np.sum(mat[i][f_ddend:fnum])
        if icount[i] > 0:
            mat[i][0] /= icount[i]

            if icount[i] == 1:
                mat[i][1] = 1
            elif icount[i] == 2:
                mat[i][2] = 1
            elif icount[i] < 5:
                mat[i][3] = 1
            elif icount[i] < 10:
                mat[i][4] = 1
            else:
                mat[i][5] = 1

    return mat, visits, tt


train_ddmat, train_visitnum, train_tt = make_ddcomb(train)
# train_ddmat, train_visitnum, train_tt = make_ddcomb(train,num_visits=5000)
valid_ddmat, valid_visitnum, valid_tt = make_ddcomb(valid)
# test_ddmat, test_visitnum, test_tt = make_ddcomb(test)

n = len(train_tt)
key = 31
ttt_key = np.zeros(n)
vtt_key = np.zeros(len(valid_tt))

for i in range(n):
    ttt_key[i] = 1 if (train_tt[i] == key) else 0

for i in range(len(valid_tt)):
    vtt_key[i] = 1 if (valid_tt[i] == key) else 0
